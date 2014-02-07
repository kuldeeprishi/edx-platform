

class MongoException(Exception):
    msg=None
    def __init__(self, *args, **kwargs):
        #Exception.__init__(self, *args, **kwargs)
        self.type=kwargs['type']
        if self.type==0:
            self.msg="Invalid Database '"+str(args[0])+"' !"
            #print self.msg
        elif self.type==1:
            self.msg="Invalid Collection '"+str(args[1])+"' in database '"+str(args[0])+"' !"
            #print self.msg
        import sys
        sys.exit(self.msg)
    def error_message(self):
        return self.msg

class MongoConnect():
    query_db=None            #database to connect
    query_collection=None    #collection name to connect
    connection_instance=None #connectin instance of query_db 
    collection_instance=None #collection instance of query_db and query_collection
    
    def __init__(self,db_name,collection_name=None):
        self.query_db=db_name
        self.query_collection=collection_name
        self.connect(collection_name)
        if db_name not in self.connection_instance.database_names():
            self.connection_instance.close()
            raise MongoException(db_name,type=0)
        if collection_name and collection_name not in self.connection_instance[db_name].collection_names():
            self.connection_instance.close()
            raise MongoException(db_name,collection_name,type=1)
        
    
    def __del__(self):
        self.connection_instance.close()
    
    def connect(self,collection_name=None):
        '''
        don't call by your self / call when you want to change the collection
        '''
        self.query_collection=collection_name #override
        try:
            from pymongo import Connection
            self.connection_instance=Connection()
            self.collection_instance=self.connection_instance[self.query_db][self.query_collection] if self.query_collection else self.connection_instance[self.query_db]
            return self.collection_instance
        except Exception,e:
            print e
    
    def getCourseByOrg(self,has_org):
        '''
        return list of courses belong to single organization
        '''
        i=1#can't enumerate 
        courses=[]
        for c in self.collection_instance.find():
            if c['_id']['category']=='course':
                if c['_id']['org'].lower()==has_org.lower():
                    course={}
                    temp=[]
                    temp.append({'NAME':c['metadata']['display_name']})
                    temp.append({'CODE':c['_id']['course']})
                    temp.append({'URL':'/courses/'+c['_id']['org']+'/'+c['_id']['course']+'/'+c['_id']['name']+'/about'})
                    course[i]=temp
                    courses.append(course)
                    i=i+1
        return courses
    
    
    def getOrgs(self):
        '''
        return list of unique organization
        '''
        orgs=set()# remove duplicate orgs
        [ orgs.add(c['_id']['org']) for c in self.collection_instance.find() if c['_id']['category']=='course']
        return list(orgs)
                
    def getAllCourse(self):
        '''
        return list of courses for all organization
        '''
        return [ {org:self.getCourseByOrg(org)} for org in self.getOrgs()]
    
    def getCourses(self,has_org=None):
        '''
        return courses of has_org else all organization courses 
        '''
        return self.getCourseByOrg(has_org) if has_org else self.getAllCourse()
    
    def describe(self):
        print "CURRENT :"
        print 'db :'+str(self.query_db)
        print 'collection :'+str(self.query_collection)
        print "-"*10
        print "ALL :"
        for db in self.connection_instance.database_names():
             print "|____[D] "+str(db)
             for c in self.connection_instance[db].collection_names():
                 print "|   |____[C] "+str(c)
             print "|"    
                 
        
        
#     def getCourse(self,has_org=None):
#         data={}
#         if has_org:
#             i=1
#             courses=[]
#             for c in self.collection_instance.find():
#                 if c['_id']['category']=='course':
# #                     print "course="+str(c)
# #                     print "display_name="+str(c['metadata']['display_name'])
#                     if c['_id']['org']==has_org:
#                         course={}
#                         temp=[]
#                         temp.append({'NAME':c['metadata']['display_name']})
#                         temp.append({'CODE':c['_id']['course']})
#                         temp.append({'URL':'----'})
#                         course[i]=temp
#                         courses.append(course)
#                         i=i+1
#             data['courses']=courses
#             
#         return data

        

        
        

