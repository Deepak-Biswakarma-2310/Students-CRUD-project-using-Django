from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Student
from .forms import AddStudentForm
from django.db import DatabaseError
from django.http import Http404

class Home(View):
    def get(self, request):
        try:
            std_data = Student.objects.all()
            return render(request, "core/home.html", {'std_data': std_data})
        except DatabaseError as e:
            # Handle the database error
            return render(request, "core/error.html", {'error': 'Error fetching student data', 'details': str(e)})

class AddStudent(View):
    def get(self, request):
        try:
            form = AddStudentForm()
            return render(request, 'core/addStudent.html', {'form':form})
        except Exception as e:
            return render(request, 'core/error.html', {'error': 'Error loading form', 'details': str(e)})
    
    def post(self, request):
        try:
            form = AddStudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                return render(request, 'core/addStudent.html', {'form':form})
        except DatabaseError as e:
            return render(request, 'core/error.html', {'error': 'Error saving student data', 'details': str(e)})
        except Exception as e:
            return render(request, 'core/error.html', {'error': 'An unexpected error occurred', 'details': str(e)})

class DeleteStudent(View):
    def post(self, request):
        try:
            data = request.POST
            id = data.get('id')
            stdData = get_object_or_404(Student, id=id)
            stdData.delete()
            return redirect('/')
        except Http404:
            return render(request, 'core/error.html', {'error': 'Student not found'})
        except DatabaseError as e:
            return render(request, 'core/error.html', {'error': 'Error deleting student', 'details': str(e)})
        except Exception as e:
            return render(request, 'core/error.html', {'error': 'An unexpected error occurred', 'details': str(e)})

class EditStudent(View):
    def get(self, request, id):
        try:
            stud = get_object_or_404(Student, id=id)
            form = AddStudentForm(instance=stud)  # Form prefilled with student data
            return render(request, 'core/editStudent.html', {'form': form})
        except Http404:
            return render(request, 'core/error.html', {'error': 'Student not found'})
        except Exception as e:
            return render(request, 'core/error.html', {'error': 'Error loading student data', 'details': str(e)})
    
    def post(self, request, id):
        try:
            stud = get_object_or_404(Student, id=id)
            form = AddStudentForm(request.POST, instance=stud)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                return render(request, 'core/editStudent.html', {'form':form})
        except DatabaseError as e:
            return render(request, 'core/error.html', {'error': 'Error updating student data', 'details': str(e)})
        except Exception as e:
            return render(request, 'core/error.html', {'error': 'An unexpected error occurred', 'details': str(e)})
