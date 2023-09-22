import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Employee


@csrf_exempt
@require_http_methods(['POST'])
def employee_add(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        Employee.objects.create(name=form['name'], password=form['password'], deptId=form['deptId'], type=form['type'])
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@require_http_methods(['GET'])
def employee_del(request):
    response = {}
    try:
        eid = request.GET.get('id')
        Employee.objects.filter(id=eid).delete()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@require_http_methods(['GET'])
def employee_info(request):
    response = {}
    try:
        name = request.GET.get('name')
        pid = request.GET.get('id')
        if name != '':
            if pid != '':
                info = Employee.objects.filter(name=name, deptId=pid)
            else:
                info = Employee.objects.filter(name=name)
        elif pid != '':
            info = Employee.objects.filter(deptId=pid)
        else:
            info = Employee.objects.filter().all()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        response['list'] = list(info.values())
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)