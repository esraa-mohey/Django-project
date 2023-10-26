from django.conf.urls import url
from .views import CreateUserAPIView, authenticate_user
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^login/$', authenticate_user),
    path('country', Get_Country),
    path('TypeofAccount', Get_TypeofAccount),
    path('Type_of_identification', Get_Type_of_identification),
    path('company/', company_info_list_and_create),
    path('company/page', company_info_list_page),
    path('company/<int:pk>', company_info_update_and_list_spacific),
]
