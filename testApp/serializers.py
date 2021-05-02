from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class AdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advisor
        fields = ['id', 'name', 'image']


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class AdvisorBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorBook
        fields = '__all__'
