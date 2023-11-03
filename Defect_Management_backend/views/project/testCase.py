import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import TestCase


# 新增需求接口
@csrf_exempt
@require_http_methods(['POST'])
def test_case_add(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        pid = json.loads(request.body)['pid']  # 项目ID
        TestCase.objects.create(title=form['title'], type=form['type'], level=form['level'],
                                creator=form['creator'], desc=form['desc'], pid=pid)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 查询接口
@csrf_exempt
@require_http_methods(['GET'])
def test_case_info(request):
    response = {}
    try:
        pid = request.GET.get('pid')  # 项目ID
        rid = request.GET.get('rid')  # 用例ID
        rtype = request.GET.get('type')
        if pid:
            if rtype:
                info = TestCase.objects.filter(pid=pid, type=rtype).values()
            else:
                info = TestCase.objects.filter(pid=pid).values()
        else:
            info = TestCase.objects.filter(id=rid).values()
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
def test_case_edit(request):
    response = {}
    try:
        rid = json.loads(request.body)['rid']  # 用例ID
        form = json.loads(request.body)['form']
        TestCase.objects.filter(id=rid).update(title=form['title'], type=form['type'], level=form['level'],
                                               creator=form['creator'], desc=form['desc'])
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 删除接口
@csrf_exempt
@require_http_methods(['GET'])
def test_case_del(request):
    response = {}
    try:
        rid = request.GET.get('rid')  # 用例ID
        TestCase.objects.filter(id=rid).delete()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '000000'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 修改状态接口
@csrf_exempt
@require_http_methods(['POST'])
def test_case_update_state(request):
    response = {}
    try:
        rid = json.loads(request.body)['rid']  # 用例ID
        state = json.loads(request.body)['newState']
        TestCase.objects.filter(id=rid).update(state=state)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 绑定需求功能
@csrf_exempt
@require_http_methods(['POST'])
def link_requirement(request):
    response = {}
    try:
        rid = json.loads(request.body)['rid']
        test_case_arr = json.loads(request.body)['selection']
        for i in test_case_arr:
            TestCase.objects.filter(id=i).update(linkId=rid)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)