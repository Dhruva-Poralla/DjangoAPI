from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments,Employee
from EmployeeApp.serializer import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage
# Create your views here.

@csrf_exempt
def DepartmentApi(request,id=0):
    if request.method=='GET':
        Department=Departments.objects.all()
        Department_serialier=DepartmentSerializer(Department,many=True)
        return JsonResponse(Department_serialier.data,safe=False)
    elif request.method=='POST':
        Department_data=JSONParser().parse(request)
        department_serialier=DepartmentSerializer(data=Department_data)
        if department_serialier.is_valid():
            department_serialier.save()
            return JsonResponse("added sucess",safe=False)
        return JsonResponse("Failed",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serialier=DepartmentSerializer.ob(department,data=department_data)
        if department_serialier.is_valid():
            department_serialier.save()
            return JsonResponse("added sucess",safe=False)
        return JsonResponse('Failed',safe=False)
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deletd",safe=False)



@csrf_exempt
def EmployeeApi(request,id=0):
    if request.method=='GET':
        employee=Employee.objects.all()
        employee_serialier=EmployeeSerializer(employee,many=True)
        return JsonResponse(employee_serialier.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serialier=EmployeeSerializer(data=employee_data)
        if employee_serialier.is_valid():
            employee_serialier.save()
            return JsonResponse("added sucess",safe=False)
        return JsonResponse("Failed",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serialier=EmployeeSerializer.ob(employee,data=employee_data)
        if employee_serialier.is_valid():
            employee_serialier.save()
            return JsonResponse("added sucess",safe=False)
        return JsonResponse('Failed',safe=False)
    elif request.method=='DELETE':
        employee=employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deletd",safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)


