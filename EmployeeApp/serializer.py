from dataclasses import fields
from pyexpat import model
from xml.sax.handler import feature_external_ges
from rest_framework import serializers
from EmployeeApp.models import Departments,Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId','DepartmentName')
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('EmployeeId','EmployeeName','Department','PhotoFileName')