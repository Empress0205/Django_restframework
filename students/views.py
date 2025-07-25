from django.shortcuts import render,HttpResponse

# Create your views here.

def students(request):
    students=[
        {'id': 1, 'name': 'John Doe', 'age': 20, 'grade': 'A'}
    ]
    
    return HttpResponse(students)

