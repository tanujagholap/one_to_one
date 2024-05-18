from django.urls import path
from .views import *


urlpatterns = [
    path('emp/', EmployeeView.as_view()),
	path('emp_info/', EmpInfoView.as_view())
]
