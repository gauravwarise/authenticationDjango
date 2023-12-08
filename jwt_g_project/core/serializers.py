from rest_framework import serializers
from .models import *

# class PostDataSerializer(serializers.Serializer):


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('id','username','password','email','first_name','last_name','date_joined','is_active','groups', 'user_permissions')
    
    def create(self, validated_data):
        # You can customize the create method if needed
        user = AuthUser().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # You can customize the update method if needed
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance