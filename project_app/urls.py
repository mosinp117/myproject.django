from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectCreateView, UserProjectsView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),  # Register a client
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),  # Fetch/Edit/Delete client
    path('projects/', ProjectCreateView.as_view(), name='project-create'),  # Add project and assign users
    path('user-projects/', UserProjectsView.as_view(), name='user-projects'),  # Retrieve assigned projects
]
