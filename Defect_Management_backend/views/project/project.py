import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Project


# 新增项目
@csrf_exempt
@require_http_methods(['POST'])
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


# 删除项目
@csrf_exempt
@require_http_methods(['DELETE'])
def project_del(request):
    response = {}
    try:
        pid = request.GET.get('id')
        Project.objects.filter(id=pid).delete()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 修改项目
@csrf_exempt
@require_http_methods(['POST'])
def project_edit(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        Project.objects.filter(id=form['id']).update(name=form['name'], desc=form['desc'], dept=form['dept'],
                                                     member=form['member'],
                                                     status=form['status'], createTime=form['createTime'])
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 查询项目
@csrf_exempt
@require_http_methods(['GET'])
def project_info(request):
    response = {}
    try:
        if request.GET.get('status'):
            status = request.GET.get('status')
        else:
            status = ''
        pid = request.GET.get('id')
        if status != '':
            info = Project.objects.filter(status=status).values()
        else:
            if pid:
                info = Project.objects.filter(id=pid).values()
            else:
                info = Project.objects.all().values()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        response['list'] = list(info)
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)