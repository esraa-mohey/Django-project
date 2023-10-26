from django.urls import path , include
from . import views
from .views import *

urlpatterns = [
    path ('', branch_stations_list),
    path ('<int:pk>', branch_stations_detail),
    path ('branch/<int:pk>', branch_stations_detail_by_branch)

    ]