from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import AppUser
from django.contrib.auth import authenticate

class AdminSerilizers(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['email', 'user_id', 'phonenumber','first_name', 'last_name', 'username','password','date_of_birth']



class AdminLoginSerilizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("username","")
        password = attrs.get("password","")
        print(email, password)
        if email and password:
            user = authenticate(username = email, password = password)
            print(user)
            if user.is_active:
                attrs["user"] = user
            else:
                msg = "unable login in to the account"
                raise ValidationError(msg)
        else:
            msg = "Provide username and password"
            raise ValidationError(msg)
        return attrs

