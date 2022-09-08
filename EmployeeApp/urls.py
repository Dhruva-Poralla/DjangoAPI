from django.urls import re_path
from DjangoAPI.settings import MEDIA_ROOT
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    re_path(r'^department$',views.DepartmentApi),
    re_path(r'^department/([0-9]+)$',views.DepartmentApi),


    re_path(r'^employee$',views.EmployeeApi),
    re_path(r'^employee/([0-9]+)$',views.EmployeeApi),

    re_path(r'^employee/savefile',views.SaveFile)


    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)