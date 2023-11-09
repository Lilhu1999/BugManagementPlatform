import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload(request):
    response = {}
    try:
        FileOperation.handle_upload_file(request.FILES.get('file'), str(request.FILES['file']))
        response['respCode'] = '000000'
        response['respMsg'] = 'success'
        response['filepath'] = FileOperation.upload_file_path(request.FILES.get('file'), str(request.FILES['file']))
        response['filename'] = FileOperation.upload_file_path(request.FILES.get('file'), str(request.FILES['file']))
    except Exception as e:
        response['respCode'] = '999999'
        response['respMsg'] = str(e)
    return JsonResponse(response)


# 图片/视频存储方法
class FileOperation:
    @staticmethod
    def handle_upload_file(file, filename):
        path = r'./templates/projectFile/'  # 文件保存路径
        print(f"filename={filename}")
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
