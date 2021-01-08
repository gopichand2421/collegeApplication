from rest_framework import serializers


from .models import AppUser


class AdminSerilizers(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['email', 'user_id', 'phonenumber','first_name', 'last_name', 'username','password','date_of_birth']