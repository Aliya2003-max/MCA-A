from django.urls import path
from .views import *

urlpatterns = [
    path('', FacultyListView.as_view(), name='faculty_list'),
    path('faculty/<int:pk>/', FacultyDetailView.as_view(), name='faculty_detail'),
    path('faculty/add/', FacultyCreateView.as_view(), name='faculty_add'),
    path('faculty/<int:pk>/edit/', FacultyUpdateView.as_view(), name='faculty_edit'),
    path('faculty/<int:pk>/delete/', FacultyDeleteView.as_view(), name='faculty_delete'),
   ]
