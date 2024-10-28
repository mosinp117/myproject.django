from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'created_at']  #--

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProjectCreateSerializer(serializers.ModelSerializer):
   
    client_name = serializers.CharField(write_only=True)
    # Use ListField with CharField for usernames   
    usernames = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'client_name', 'usernames','start_date', 'end_date'] 

    
    
    def create(self, validated_data):
        # print(validated_data)
        client_name = validated_data.pop('client_name')
        usernames = validated_data.pop('usernames')

        # Get the client and users from validated data
        client = Client.objects.get(name=client_name)
        users = User.objects.filter(username__in=usernames)

        # Create the project and add users
        project = Project.objects.create(client=client, **validated_data)
        project.users.set(users)
        return project