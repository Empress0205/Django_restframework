from django.urls import path

from .import views

urlpatterns = [
    path('students/', views.studentsView, name='students'),
    path('students/<int:pk>/', views.studentDetailView, name='student_detail'),
    path('employees/', views.Employees.as_view(), name='employees'),
    path('employees/<int:pk>/', views.EmployeesDetails.as_view(), name='employee_detail'),
]
