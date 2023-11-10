import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from Defect_Management_backend.models import ProjectFile


# 项目文件查询接口
@csrf_exempt
@require_http_methods(['GET'])
def document_info(request):
    response = {}
    try:
        pid = request.GET.get('pid')
        fileName = request.GET.get('fileName')
        creator = request.GET.get('creator')
        if pid:
            if fileName and creator:
                info = ProjectFile.objects.filter(pid=pid, fileName__contains=fileName, creator__contains=creator).values()
            elif fileName:
                info = ProjectFile.objects.filter(pid=pid, fileName__contains=fileName).values()
            elif creator:
                info = ProjectFile.objects.filter(pid=pid, creator__contains=creator).values()
            else:
                info = ProjectFile.objects.filter(pid=pid).values()
        else:
            info = []  # 待设计
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        response['list'] = list(info)
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 项目文件上传接口
@csrf_exempt
def upload(request):
    response = {}
    try:
        pid = request.POST.get('pid')
        creator = request.POST.get('creator')
        FileOperation.handle_upload_file(request.FILES.get('file'), str(request.FILES['file']))
        filepath = FileOperation.upload_file_path(request.FILES.get('file'), str(request.FILES['file']))
        filename = FileOperation.upload_file_name(request.FILES.get('file'), str(request.FILES['file']))
        ProjectFile.objects.create(fileName=filename, filePath=filepath, creator=creator, pid=pid)
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 存储方法
class FileOperation:
    @staticmethod
    def handle_upload_file(file, filename):
        path = r'./templates/projectFile/'  # 文件保存路径
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + filename, 'wb') as destination:
            for chunk in file.chunks():
                # print(chunk)
                destination.write(chunk)

    # return文件路径
    @staticmethod
    def upload_file_path(file, filename):
        path = r'./file/projectFile/' + f"{filename}"
        return path

    # return文件名
    @staticmethod
    def upload_file_name(file, filename):
        name = f"{filename}"
        return name
