from rest_framework import serializers
from .models import branch
from branch_stationss.serialiazers import list_branch_stat_Serializer


class branchSerializer(serializers.ModelSerializer):

    class Meta:
        model = branch
        fields ="__all__"

class listbranchSerializer(serializers.ModelSerializer):
    branch_station = list_branch_stat_Serializer(many = True)
    class Meta:
        model = branch
        fields ="__all__"
