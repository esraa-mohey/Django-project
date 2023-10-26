from rest_framework.decorators import api_view 
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import branch_station
from .serialiazers import *
from rest_framework import status
from django.core import serializers
from rest_framework.response import Response
from news.serialiazers import PageNumberPagination
#from rest_framework.pagination import PageNumberPagination


@api_view(['GET', 'POST'])
def branch_stations_list(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        branch_stationss = branch_station.objects.all()
        context = paginator.paginate_queryset(branch_stationss, request)
        time = request.query_params.get('station_id', None)
        if time is not None:
            branch_stationss = branch_stationss.filter(Pass__icontains=time)

        branch_stationss_Serializer = getbranch_stations_Serializer(context, many=True)
        return paginator.get_paginated_response(branch_stationss_Serializer.data)
        # return JsonResponse(branch_stationss_Serializer.data ,safe=False)

    elif request.method == 'POST':
        branch_stationss_Serializer = branch_stations_Serializer(
            data=request.data)
        if branch_stationss_Serializer.is_valid():
            branch_stationss_Serializer.save()
            return JsonResponse(branch_stationss_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(branch_stationss_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def branch_stations_detail(request, pk):
    branch_stationss = branch_station.objects.get(pk=pk)
    if request.method == 'GET':
        branch_stationss_Serializer = branch_stations_Serializer(branch_stationss)
        return JsonResponse(branch_stationss_Serializer.data)

    elif request.method == 'PUT':
        serializer = branch_stations_Serializer(branch_stationss, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         


@api_view(['GET'])
def branch_stations_detail_by_branch(request, pk):
    
    branch_stationss = branch_station.objects.filter(branch_id=pk)
    if request.method == 'GET':
        branch_stationss_Serializer = branch_stat_Serializer( branch_stationss, many=True)
        return Response(branch_stationss_Serializer.data)

