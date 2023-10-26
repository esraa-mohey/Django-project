from django.urls import path , include
from . import views
from .views import *
#from .GR_views import GoRegion_detail

urlpatterns = [
    path ('', stations_list),
    path ('page', stations_list_with_paginate),
    path ('<int:pk>', stations_detail),
    path ('operationCode/<int:pk>', stations_operationCode_detail),


]
