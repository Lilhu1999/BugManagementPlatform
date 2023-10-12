from django.urls import path,include

from Defect_Management_backend.views.user.departmentTree import department_info

urlpatterns = [
    path('', include('Defect_Management_backend.views.user.urls')),
    path('', include('Defect_Management_backend.views.project.urls')),
]
