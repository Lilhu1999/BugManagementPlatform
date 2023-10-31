import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Defect


# 新增需求接口
@csrf_exempt
@require_http_methods(['POST'])
def defect_add(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        pid = json.loads(request.body)['pid']  # 项目ID
        Defect.objects.create(title=form['title'], priority=form['priority'], iteration=form['iteration'],
                              handler=form['handler'], creator=form['creator'],
                              desc=form['desc'], importance=form['importance'], pid=pid)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 查询接口
@csrf_exempt
@require_http_methods(['GET'])
def defect_info(request):
    response = {}
    try:
        pid = request.GET.get('pid')  # 项目ID
        rid = request.GET.get('rid')  # 缺陷ID
        if pid:
            info = Defect.objects.filter(pid=pid).values()
        else:
            info = Defect.objects.filter(id=rid).values()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        response['list'] = list(info)
    except Exception as e:
        response['respCode'] = '000000'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 修改接口
@csrf_exempt
@require_http_methods(['POST'])
def defect_edit(request):
    response = {}
    try:
        rid = json.loads(request.body)['rid']
        form = json.loads(request.body)['form']
        Defect.objects.filter(id=rid).update(title=form['title'], priority=form['priority'],
                                             iteration=form['iteration'], importance=form['importance'],
                                             handler=form['handler'], creator=form['creator'],
                                             desc=form['desc'])
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 删除接口
@csrf_exempt
@require_http_methods(['GET'])
def defect_del(request):
    response = {}
    try:
        rid = request.GET.get('rid')  # 缺陷ID
        Defect.objects.filter(id=rid).delete()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '000000'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 修改状态接口
@csrf_exempt
@require_http_methods(['POST'])
def defect_update_state(request):
    response = {}
    try:
        rid = json.loads(request.body)['rid']
        state = json.loads(request.body)['newState']
        Defect.objects.filter(id=rid).update(state=state)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)
