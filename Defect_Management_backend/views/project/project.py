import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Project


# 新增项目
def project_add(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        Project.objects.create(name=form['name'], desc=form['desc'], dept=form['dept'], member=form['member'],
                               status=form['status'], createTime=form['createTime'])
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)
