import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Iteration


# 新增迭代
@csrf_exempt
@require_http_methods(['POST'])
def iteration_add(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        pid = json.loads(request.body)['pid']
        if form['state'] == '关闭':
            Iteration.objects.create(title=form['title'], start=form['start'], end=form['end'], state=form['state'],
                                     pid=pid)
        else:
            Iteration.objects.create(title=form['title'], start=form['start'], end=form['end'], pid=pid)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 删除迭代
@csrf_exempt
@require_http_methods(['DELETE'])
def iteration_del(request):
    response = {}
    try:
        rid = request.GET.get('rid')
        Iteration.objects.filter(id=rid).delete()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 修改迭代
@csrf_exempt
@require_http_methods(['POST'])
def iteration_edit(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        rid = json.loads(request.body)['rid']
        if form['state']:
            Iteration.objects.filter(id=rid).update(state=form['state'])
        else:
            Iteration.objects.filter(id=rid).update(title=form['title'], start=form['start'], end=form['end'])
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 查看迭代
@csrf_exempt
@require_http_methods(['GET'])
def iteration_info(request):
    response = {}
    try:
        pid = request.GET.get('pid')
        info = Iteration.objects.filter(pid=pid).values()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        response['list'] = list(info)
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)
