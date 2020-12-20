"""LYNews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
    网站爬虫：爬取网站新闻，类型，关键字，
    保存数据库：编号id, 阅读量，推送量,日期
    随机获取不同的新闻 到字典 {'爱好':[id...]}
    提供API：
    手机端获取：
    H5
    小程序
    web端
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app01.urls', namespace='app01')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  为了网页显示上传的图片/文件
