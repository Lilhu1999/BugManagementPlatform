import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import Employee


# 登录接口
@csrf_exempt
@require_http_methods(['POST'])
def user_login(request):
    response = {}
    try:
        form = json.loads(request.body)['form']
        if Employee.objects.filter(name=form['username']):
            info = Employee.objects.filter(name=form['username']).values()
            password = list(info)[0]['password']
            if list(info)[0]['type'] == 0:
                user_type = '普通用户'
            else:
                user_type = '管理员'
            if password == form['password']:
                response['respCode'] = '000000'
                response['respMsg'] = 'success'
                response['user_type'] = user_type
            else:
                response['respCode'] = '999999'
                response['respMsg'] = '用户名或密码错误'
        else:
            response['respCode'] = '999999'
            response['respMsg'] = '用户名不存在'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)

# 修改密码
@csrf_exempt
@require_http_methods(['POST'])
def password_edit(request):
    response = {}
    try:
        new_password = json.loads(request.body)['password']
        username = json.loads(request.body)['username']
        Employee.objects.filter(username=username).update(password=new_password)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)