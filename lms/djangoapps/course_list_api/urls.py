
from django.conf.urls import patterns,url
#from django.http import HttpResponse



urlpatterns = patterns('course_list_api.views',
    url(r'^courses$','v_list_course'),
    
)