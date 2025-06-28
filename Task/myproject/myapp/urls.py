from django.urls import path
from . import views
urlpatterns = [
   path('insert_Student/',views.insert_Student, name='insert_Student'),
   path('view_Student/', views.view_Student,  name = 'view_Student'),
# other paths as needed
]

# Create your tests here.
