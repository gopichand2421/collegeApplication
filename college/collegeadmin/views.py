from django.shortcuts import render

from django.contrib.auth import login,logout
from .adminserilizers import AdminSerilizers
from .models import AppUser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .adminserilizers import AdminLoginSerilizer




@api_view(['GET','POST'])
def AdminRegister(request):

    if request.method == 'GET':
        user = AppUser.objects.all()
        user_serilizer = AdminSerilizers(user, many=True)
        return Response(user_serilizer.data)
    elif request.method == 'POST':
        print(request.data)
        user_serilizer = AdminSerilizers(data= request.data)
        if user_serilizer.is_valid():
            email = request.data['email']
            phonenumber = request.data['phonenumber']
            firstname = request.data['first_name']
            lastname = request.data['last_name']
            username = request.data['username']
            password = request.data['password']
            dateofbirth = request.data['date_of_birth']
            AppUser.objects.create_user(email=email,phonenumber=phonenumber,firstname=firstname,lastname=lastname,username=username,password=password,date_of_birth = dateofbirth)
            return Response(user_serilizer.data, status= status.HTTP_201_CREATED)
        return Response(user_serilizer.errors, status = status.HTTP_400_BAD_REQUEST)


class ExampleView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user' : request.data,
            'auth' : request.auth
        }
        return Response(content)


class LoginView(APIView):
    def post(self, request):
        serilizer = AdminLoginSerilizer(data= request.data)
        serilizer.is_valid(raise_exception= True)
        user = serilizer.validated_data["user"]
        login(request, user)
        token,create = Token.objects.get_or_create(user = user)
        return Response({"token": token.key, "status":200},status=200)

class LogOutView(APIView):
    authentication_classes = [TokenAuthentication,]
    def post(self, request):
        logout(request)
        return Response(status=204)


