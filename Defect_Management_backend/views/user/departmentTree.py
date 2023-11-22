import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Department


# 转化为树结构
def tree(dept_arr, parent):
    tree_data = []
    for item in dept_arr:
        if item['parentId'] == parent:
            if item['hasChildren'] == 'true':
                item['children'] = tree(dept_arr, int(item['id']))
            tree_data.append(item)
    return tree_data


# 查询接口
@csrf_exempt
def department_info(request):
    response = {}
    try:
        info = Department.objects.filter().all()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        arr = tree(list(info.values()), 0)
        response['list'] = arr
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@require_http_methods(['POST'])
def department_add(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        Department.objects.create(name=form['name'], parentId=form['id'], hasChildren='false')
        Department.objects.filter(id=form['id']).update(hasChildren='true')
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)
