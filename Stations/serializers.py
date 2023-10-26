from rest_framework import serializers
from .models import *
from governorate.serialiazers import *


class StationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = stations
        fields = "__all__"

class Stations_put_Serializer(serializers.ModelSerializer):
    class Meta:
        model = stations
        fields = ('governorate_id','name')

class Stations_list_Serializer(serializers.ModelSerializer):
    governorate_id = GoveeListSerializer(many=False)

    class Meta:

        model = stations
        fields = "__all__"


class Stations_list_rev_Serializer(serializers.ModelSerializer):
    # governorate_id = GoveeListSerializer(many=False)
    class Meta:

        model = stations
        fields = ('id',)

class Stations_name_Serializer(serializers.ModelSerializer):
   
    class Meta:

        model = stations
        fields = ('id','name')