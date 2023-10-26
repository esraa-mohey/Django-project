from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import branch
from .serializer import *
from rest_framework import status
#from rest_framework.pagination import PageNumberPagination
from news.serialiazers import PageNumberPagination
@api_view(['GET', 'POST'])
def branch_list(request):
    if request.method == 'GET':
        # paginator = PageNumberPagination()
        branches = branch.objects.all()
        # context = paginator.paginate_queryset(branches, request)
        brn = request.query_params.get('en_name', None)
        if brn is not None:
            branches = branches.filter(Pass__icontains=brn)

        branch_Serializer = branchSerializer(branches, many=True)
        # return paginator.get_paginated_response(branch_Serializer.data)

        return JsonResponse(branch_Serializer.data ,safe=False)


    elif request.method == 'POST':
        # branch_data = JSONParser().parse(request)
        branch_Serializer = branchSerializer(data=request.data)
        if branch_Serializer.is_valid():
            branch_Serializer.save()
            return JsonResponse(branch_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(branch_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def branch_list_page(request):
     paginator = PageNumberPagination()
     branches = branch.objects.all()
     context = paginator.paginate_queryset(branches, request)
     brn = request.query_params.get('en_name', None)
     if brn is not None:
         branches = branches.filter(Pass__icontains=brn)

     branch_Serializer = branchSerializer(context, many=True)
     return paginator.get_paginated_response(branch_Serializer.data)


@api_view(['GET'])
def branch_detail(request, pk):
    try:
        branches = branch.objects.get(pk=pk)
    except branches.DoesNotExist:
        return JsonResponse({'message': 'This line does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        branch_Serializer = branchSerializer(branches)
        return JsonResponse(branch_Serializer.data)
