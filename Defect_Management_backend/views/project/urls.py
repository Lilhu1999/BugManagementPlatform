from django.urls import path, include

from Defect_Management_backend.views.project.project import project_add, project_del, project_info, project_edit

from Defect_Management_backend.views.project.requirement import requirement_add, requirement_info

urlpatterns = [
    path('project/add/', project_add),
    path('project/del/', project_del),
    path('project/edit/', project_edit),
    path('project/info/', project_info),
    path('project/requirement/add/', requirement_add),
    path('project/requirement/info/', requirement_info),
]
