#from django.shortcuts import render

from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import stations
from .serializers import*
#from region.models import Region
from rest_framework.response import Response
#from region.serialiazers import RegionSerializer
from rest_framework import status
#from rest_framework.pagination import PageNumberPagination
from news.serialiazers import PageNumberPagination
from django.db.models import Q


@api_view(['GET', 'POST'])
def stations_list(request):
    if request.method == 'GET':
        Station_Data = stations.objects.filter(IsActive=True)
        stat = request.query_params.get('nameEn', None)
        if stat is not None:
            Station_Data = Station_Data.filter(Pass__icontains=stat)

        Stations_Serializer = Stations_list_Serializer(Station_Data, many=True)
        return Response(Stations_Serializer.data)

    elif request.method == 'POST':

        Stations_Serializer = StationsSerializer(data=request.data)

        if Stations_Serializer.is_valid():
            Stations_Serializer.save()
            return Response(Stations_Serializer.data, status=status.HTTP_201_CREATED)
        return Response(Stations_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def stations_list_with_paginate(request):
    paginator = PageNumberPagination()
    Station_Data = stations.objects.all()
    pages = request.GET.get('page')
    # if pages == '0':
    # context = paginator.paginate_queryset(Station_Data, request)
    # Stations_Serializer = Stations_list_Serializer(context, many=True)
    # cart_details = paginator.page(1)
    # return cart_details.get_paginated_response(Stations_Serializer.data)
    # Stations_Serializer = Stations_list_Serializer(Station_Data, many=True)
    # serializer = self.get_pagination_serializer(1)
    # return paginator.get_paginated_response(Stations_Serializer.data)

    context = paginator.paginate_queryset(Station_Data, request)
    stat = request.query_params.get('key')
    # opera = request.data.get('operationcode')
    if stat is not None:
        try:
            val = int(stat)
            Station_Data = Station_Data.filter(
                Q(operationCode=stat) | Q(governorate_id=stat))
            Stations_Serializer = Stations_list_Serializer(
                Station_Data, many=True)
            return JsonResponse({"results": Stations_Serializer.data}, safe=False)
        except ValueError:
            Station_Data = Station_Data.filter(
                Q(name__0__ar__icontains=stat) | Q(name__0__en__icontains=stat))
            Stations_Serializer = Stations_list_Serializer(
                Station_Data, many=True)
            return JsonResponse({"results": Stations_Serializer.data}, safe=False)
    # if opera is not None:
    #     Station_Data = Station_Data.filter(operationCode=opera)
    #     Stations_Serializer = Stations_list_Serializer(Station_Data, many=True)
    #     return JsonResponse(Stations_Serializer.data)
    Stations_Serializer = Stations_list_Serializer(context, many=True)
    return paginator.get_paginated_response(Stations_Serializer.data)


@api_view(['GET', 'PUT'])
def stations_detail(request, pk):

    station = stations.objects.get(id=pk)
    if request.method == 'GET':
        Stations_Serializer = Stations_list_Serializer(station)
        return JsonResponse(Stations_Serializer.data)

    elif request.method == "PUT":
        Stations_Serializer = Stations_put_Serializer(
            station, data=request.data)
        if Stations_Serializer.is_valid(raise_exception=True):
            Stations_Serializer.save()
            return Response(Stations_Serializer.data, status=status.HTTP_201_CREATED)
        return Response(Stations_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse(Stations_Serializer.data)


@api_view(['GET'])
def stations_operationCode_detail(request, pk):

    station = stations.objects.get(operationCode=pk)
    Stations_Serializer = Stations_list_Serializer(station)
    return JsonResponse(Stations_Serializer.data)
