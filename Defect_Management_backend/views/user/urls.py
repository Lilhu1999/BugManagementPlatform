from django.urls import path,include

from Defect_Management_backend.views.user.departmentTree import department_info, department_add
from Defect_Management_backend.views.user.login import user_login
from Defect_Management_backend.views.user.member import employee_add, employee_del, employee_info

urlpatterns = [
    path('getTree/', department_info),
    path('dept/add/', department_add),
    path('emp/add/', employee_add),
    path('emp/del/', employee_del),
    path('emp/info/', employee_info),
    path('login/', user_login),
]