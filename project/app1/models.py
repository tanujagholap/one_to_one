from django.db import models


class Employee(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.first_name}, {self.last_name}'


class EmpInfo(models.Model):
	employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
	emp_sal = models.FloatField()
	emp_add = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.employee}, {self.emp_sal}, {self.emp_add}'
