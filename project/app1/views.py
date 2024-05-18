from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import EmployeeSerializers, EmpInfoSerializers, Employee, EmpInfo


class EmployeeView(ListCreateAPIView):
	serializer_class = EmployeeSerializers
	queryset = Employee.objects.all()


class EmpInfoView(ListCreateAPIView):
	serializer_class = EmpInfoSerializers
	queryset = EmpInfo.objects.all()
