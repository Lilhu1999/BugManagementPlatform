import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Requirement


# 新增需求接口
@csrf_exempt
@require_http_methods(['POST'])
def requirement_add(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        pid = json.loads(request.body)['pid']
        Requirement.objects.create(title=form['title'], priority=form['priority'], iteration=form['iteration'],
                                   state=form['state'], handler=form['handler'], start=form['start'], end=form['end'],
                                   pid=pid)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 查询接口
@csrf_exempt
@require_http_methods(['GET'])
def requirement_info(request):
    response = {}
    try:
        pid = request.GET.get('pid')
        info = Requirement.objects.filter(pid=pid).values()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        response['list'] = list(info)
    except Exception as e:
        response['respCode'] = '000000'
        response['respMsg'] = str(e)
    return JsonResponse(response)
