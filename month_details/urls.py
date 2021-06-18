from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from month_details import views
import month_details
urlpatterns = [
    path("",views.month),
    path("<monthname>/",views.monthname),#,name='monthname'
]
#py tho ala iyali django lo monthname is dynamic so akada em vachina it will be sent as a parameter to views monthname