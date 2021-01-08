from django.shortcuts import render

from .adminserilizers import AdminSerilizers
from .models import AppUser
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




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




