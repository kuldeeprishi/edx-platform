# Create your views here.


import json
from django.http import HttpResponse
from xmodule.modulestore.django import modulestore
from .mongo import *
from .conf import db_name,collection_name


def v_list_course(req):
    
    org_name=req.GET.get('org',None)

    '''
    Modulestore backed by Mongodb.

    Stores individual XModules as single documents with the following
    structure:
    
    {
    '_id': <location.as_dict>,
    'metadata': <dict containing all Scope.settings fields>
    'definition': <dict containing all Scope.content fields>
    'definition.children': <list of all child location.url()s>
    }
     modulestore  is xmodule.modulestore.mixed.MixedModuleStore object
    
    
    _____________
      
     modulestore().get_courses()[0] will return 
     
     CourseDescriptorWithMixins(
         <xmodule.modulestore.mongo.base.CachingDescriptorSystem object at 0x7f69488d9b90>,\
         <DbModel <xmodule.modulestore.mongo.base.MongoKeyValueStore object at 0x7f69488d9590>>,
         ScopeIds(user_id=None, block_type=u'course',
             def_id=Location(u'i4x', u'BRENTWOOD', u'PY001', u'course', u'PY001URL', None),
             usage_id=Location(u'i4x', u'BRENTWOOD', u'PY001', u'course', u'PY001URL', None)))

    '''
    
    
    data = {
        'courses': MongoConnect(db_name,collection_name).getCourses(org_name)
    }
    
    return HttpResponse(json.dumps(data, indent=4),mimetype='application/json')





    
        
         
    
#from datetime import datetime
#from pytz import UTC
#from dogapi import dog_stats_api
#@dog_stats_api.timed('edxapp.heartbeat')
#from django.http import HttpResponse
#from django.shortcuts import render_to_response
#from django.contrib.auth.models import User


#from xmodule import  modulestore #ModuleStoreWriteBase,
# def get_courses(self):
#         '''
#         Returns a list of course descriptors.
#         '''
#         # TODO (vshnayder): Why do I have to specify i4x here?
#         course_filter = Location("i4x", category="course")
#         return [
#             course
#             for course
#             in self.get_items(course_filter)
#             if not (
#                 course.location.org == 'edx' and
#                 course.location.course == 'templates'
#             )
#         ]


   