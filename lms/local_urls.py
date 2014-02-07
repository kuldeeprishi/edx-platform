
from django.conf.urls import patterns,url
from django.http import HttpResponse
from django.conf.urls import  include


urlpatterns = patterns('',
    url(r'^list_api/',include('course_list_api.urls')),
)


