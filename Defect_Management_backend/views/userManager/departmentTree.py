from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Defect_Management_backend.models import Department


def tree_set(val):
    tree = []
    temp = []
    for i in val:
        if i['parentId']:
            temp.append(i)
        else:
            tree.append(i)
    while temp != 0:
        for j in temp:

            if j['parentId']:
    return tree



# 查询接口
@csrf_exempt
def department_info(request):
    response = {}
    try:
        info = Department.objects.filter().all()
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        response['list'] = list(info.values())
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)
