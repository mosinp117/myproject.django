from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from project_app.models import Client, Project
from project_app.serializer import ClientSerializer, ProjectCreateSerializer
from django.contrib.auth.models import User

# Register a client
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Fetch, Edit, and Delete client info
class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Add new projects for a client and assign users
class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        print(self.request.data.get('client_name'))
        print(self.request.data.get('usernames'))
        try:
            # client = Client.objects.get(name=self.request.data.get('client_name'))
            # users = User.objects.filter(username__in=self.request.data.get('usernames'))
            serializer.save()
        except Exception as ex:
            print(ex)

# Retrieve assigned projects for logged-in user
class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectCreateSerializer



    def get_queryset(self):
        return Project.objects.filter(users=self.request.user)

