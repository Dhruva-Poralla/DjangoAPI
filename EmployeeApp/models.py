from msilib.schema import Class
from django.db import models

class Departments(models.Model):

    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=100)

class Employee(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=500)
    Department=models.CharField(max_length=500)
    PhotoFileName=models.CharField(max_length=500)


