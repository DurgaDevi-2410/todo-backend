from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Category

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'color']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('user', 'date') 
        # Note: date is auto_now_add, so read_only. 
        # Frontend sends 'date' but usually we want creation date. 
        # If frontend wants to BACKDATE tasks, we should remove auto_now_add=True in models.
        # But 'date' in frontend seems to be creation date.
