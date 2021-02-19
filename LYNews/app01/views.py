from django.shortcuts import render,  HttpResponse
from django.http.response import JsonResponse


def index(req):
    return render(req,"index.html",{'msg':'OK','ucode':'Zhang Sanfeng','uname':'张三丰'})


def content(req):
    return render(req,"content.html",{'msg':'OK','ucode':'Zhang Sanfeng','uname':'张三丰'})

def contact(req):
    return render(req,"contact.html",{'msg':'OK','ucode':'Zhang Sanfeng','uname':'张三丰'})


def upload(request):
    """
    保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
    但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
        filename = request.FILES['file'].name
        # 在项目目录下新建一个文件
        with open(filename, "wb") as f:
            # 从上传的文件对象中一点一点读
            for chunk in request.FILES["file"].chunks():
                # 写入本地文件
                f.write(chunk)
        return HttpResponse("上传OK")


def list(request):
    return JsonResponse({'msg':'OK', 'data':[]})


