from rest_framework import serializers
from .models import *


class EmployeeSerializers(serializers.ModelSerializer):
	class Meta:
	   model = Employee
	   fields = '__all__'


class EmpInfoSerializers(serializers.ModelSerializer):
	class Meta:
		model = EmpInfo
		fields = '__all__'
