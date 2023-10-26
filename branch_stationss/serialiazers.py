from rest_framework import serializers
from .models import branch_station
from branches.models import branch
# from branches.serializer import branchSerializer
from Stations.serializers import StationsSerializer , Stations_name_Serializer
from Stations.models import stations

class branch_stations_Serializer(serializers.ModelSerializer):

    class Meta:
       model = branch_station
       fields =  '__all__'



class branch_stat_Serializer(serializers.ModelSerializer):
    station_id = Stations_name_Serializer()
    class Meta:
       model = branch_station
       fields = ('id','idx','KM','station_id')


       

class list_branch_stat_Serializer(serializers.ModelSerializer):
    station_id = StationsSerializer()
    class Meta:
       model = branch_station
       fields = ('id','idx','station_id')

class getbranch_stations_Serializer(serializers.ModelSerializer):
    # branch_id = branchSerializer()
    station_id = StationsSerializer()
    class Meta:
       model = branch_station
       fields =  '__all__'
