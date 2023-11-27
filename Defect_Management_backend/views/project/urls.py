from django.urls import path, include

from Defect_Management_backend.views.project.defect import defect_add, defect_info, defect_edit, defect_del, \
    defect_update_state, link_test_case
from Defect_Management_backend.views.project.iteration import iteration_add, iteration_del, iteration_edit, \
    iteration_info, iteration_update_state
from Defect_Management_backend.views.project.project import project_add, project_del, project_info, project_edit

from Defect_Management_backend.views.project.requirement import requirement_add, requirement_info, requirement_edit, \
    requirement_del, requirement_update_state
from Defect_Management_backend.views.project.testCase import test_case_add, test_case_edit, test_case_del, \
    test_case_update_state, test_case_info, link_requirement
from Defect_Management_backend.views.project.document import upload, document_info, download, document_del

urlpatterns = [
    path('project/add/', project_add),
    path('project/del/', project_del),
    path('project/edit/', project_edit),
    path('project/info/', project_info),
    path('project/requirement/add/', requirement_add),
    path('project/requirement/info/', requirement_info),
    path('project/requirement/edit/', requirement_edit),
    path('project/requirement/del/', requirement_del),
    path('project/requirement/updateState/', requirement_update_state),
    path('project/defect/add/', defect_add),
    path('project/defect/info/', defect_info),
    path('project/defect/edit/', defect_edit),
    path('project/defect/del/', defect_del),
    path('project/defect/updateState/', defect_update_state),
    path('project/defect/link/', link_test_case),
    path('project/testcase/add/', test_case_add),
    path('project/testcase/info/', test_case_info),
    path('project/testcase/edit/', test_case_edit),
    path('project/testcase/del/', test_case_del),
    path('project/testcase/updateState/', test_case_update_state),
    path('project/testcase/link/', link_requirement),
    path('upload/', upload),
    path('download/', download),
    path('project/document/info/', document_info),
    path('project/document/del/', document_del),
    path('project/iteration/add/', iteration_add),
    path('project/iteration/del/', iteration_del),
    path('project/iteration/edit/', iteration_edit),
    path('project/iteration/info/', iteration_info),
    path('project/iteration/updateState/', iteration_update_state),
]
