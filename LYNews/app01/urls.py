from django.urls import path
from app01 import views

app_name = 'app01'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'content', views.content, name='content'),
    path(r'contact', views.contact, name='contact'),
    path(r'list', views.list, name='list'),
]
# html 就可以使用url别名 {% url 'appName:index' %} 方便维护

