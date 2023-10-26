from django.urls import path , include
from . import views
from .views import *

urlpatterns = [
    path ('', branch_list),
    path ('page', branch_list_page),
    path ('<int:pk>', branch_detail)
]
