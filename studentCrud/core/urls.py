from django.urls import path
# from . import views # we are not using this because we have created class based views
from .views import Home, AddStudent, DeleteStudent, EditStudent # importing class based views

urlpatterns = [
    path('', Home.as_view(), name='home'), # .as_view() used for class based views otherwise it will not render the URL
    path('addStudent/', AddStudent.as_view(), name='addStudent'),
    path('deleteStudent/', DeleteStudent.as_view(), name='deleteStudent'),
    path('editStudent/<int:id>/', EditStudent.as_view(), name='editStudent'),
]