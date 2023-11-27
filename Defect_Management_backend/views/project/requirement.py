import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Requirement, Iteration


# 新增需求接口
@csrf_exempt
@require_http_methods(['POST'])
def requirement_add(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        pid = json.loads(request.body)['pid']  # 项目ID
        iteration_title = Iteration.objects.filter(id=form['iteration']).values('title')
        Requirement.objects.create(title=form['title'], priority=form['priority'], iteration=iteration_title, iterationId=form['iteration'],
                                   handler=form['handler'], start=form['start'], end=form['end'],
                                   desc=form['desc'], pid=pid)
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
        pid = request.GET.get('pid')  # 项目ID
        rid = request.GET.get('rid')  # 需求ID
        iteration_id = request.GET.get('iterationId')    # 迭代ID
        if pid:
            info = Requirement.objects.filter(pid=pid).values()
        elif rid:
            info = Requirement.objects.filter(id=rid).values()
        else:
            info = Requirement.objects.filter(iterationId=iteration_id).values()
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
def requirement_edit(request):
    response = {}
    try:
        rid = json.loads(request.body)['rid']
        form = json.loads(request.body)['form']
        iteration_title = Iteration.objects.filter(id=form['iteration']).values('title')
        Requirement.objects.filter(id=rid).update(title=form['title'], priority=form['priority'],
                                                  iterationId=form['iteration'], iteration=iteration_title,
                                                  handler=form['handler'], start=form['start'], end=form['end'],
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
def requirement_del(request):
    response = {}
    try:
        rid = request.GET.get('rid')  # 需求ID
        Requirement.objects.filter(id=rid).delete()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '000000'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 修改状态接口
@csrf_exempt
@require_http_methods(['POST'])
def requirement_update_state(request):
    response = {}
    try:
        rid = json.loads(request.body)['rid']
        state = json.loads(request.body)['newState']
        Requirement.objects.filter(id=rid).update(state=state)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)
