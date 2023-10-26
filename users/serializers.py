from nationality.serializers import Nationality_Serializer
from rest_framework import serializers
from.models import *


class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'middle_Name',
                  'gender', 'typeofidentification', 'Number_of_identification', 'Home_address', 'typeOfAccount',
                  'mobile', 'date_of_Birth', 'password', 'country', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}


class Country_Serializer(serializers.ModelSerializer):
    nationality = Nationality_Serializer()

    class Meta:
        model = Country
        fields = "__all__"


class TypeofAccount_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TypeofAccount
        fields = "__all__"


class Type_of_identification_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Type_of_identification
        fields = "__all__"


class Company_Info_Serializer(serializers.ModelSerializer):
    class Meta:
        model = company_info
        fields = "__all__"
