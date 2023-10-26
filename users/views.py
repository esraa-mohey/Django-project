from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import *
from rest_framework.pagination import PageNumberPagination
from ernst import settings
from rest_framework_jwt.settings import api_settings
import jwt


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data

        serializer = UserSerializer(data=user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"data":  serializer.errors, 'message': 'هذا الحساب موجود بالفعل'}, status=status.HTTP_400_BAD_REQUEST)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({'message': 'هذا الحساب موجود بالفعل', data=serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):

    try:
        email = request.data['email']
        password = request.data['password']

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        user = User.objects.get(username=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token

                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            return Response({'message': 'يوجد خطاء فى الحساب'}, status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        res = {'message': 'يوجد خطاء فى الحساب'}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Get_Country(request):
    if request.method == 'GET':
        snippets = Country.objects.all()
        serializer = Country_Serializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Get_TypeofAccount(request):
    if request.method == 'GET':
        snippets = TypeofAccount.objects.all()
        serializer = TypeofAccount_Serializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def Get_Type_of_identification(request):
    if request.method == 'GET':
        snippets = Type_of_identification.objects.all()
        serializer = Type_of_identification_Serializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def company_info_list_and_create(request):
    if request.method == 'GET':
        # paginator = PageNumberPagination()
        snippets = company_info.objects.all()
        # context = paginator.paginate_queryset(snippets, request)
        serializer = Company_Info_Serializer(snippets, many=True)
        # return paginator.get_paginated_response(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Company_Info_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def company_info_list_page(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        snippets = company_info.objects.all()
        context = paginator.paginate_queryset(snippets, request)
        serializer = Company_Info_Serializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)
        # return Response(serializer.data)


@api_view(['PUT', 'GET'])
def company_info_update_and_list_spacific(request, pk):

    snippets = company_info.objects.get(id=pk)
    if request.method == 'GET':
        serializer = Company_Info_Serializer(snippets)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Company_Info_Serializer(snippets, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
