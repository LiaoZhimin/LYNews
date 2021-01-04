from django.contrib import admin
from app01.models import Category, Tags, Article


# Register your models here.
@admin.register(Article)  # 绑定模型到表格
class  ArticleAdmin(admin.ModelAdmin):  
    list_display = ('id','name', 'category', 'tags', 'excerpt','body', 'views','photo','created_time')  # 表格显示的列，model的属性
    list_per_page = 50  # list_per_page设置每页显示多少条记录，默认是100条
    ordering = ('-id',)  # ordering设置默认排序字段，负号表示降序排序
    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    list_editable = [ 'name', 'category', 'tags', 'excerpt','body']     
    # fk_fields = ['category']  # fk_fields 设置显示外键字段
    list_display_links = ('id')  # 设置哪些字段可以点击进入编辑界面
    search_fields = ['name', 'category', 'tags', 'excerpt','body']  # 搜索栏
    list_filter = ['category', 'tags']  # 右侧筛选
    date_hierarchy = 'created_time'  # 日期筛选属性


admin.site.site_header = '管理后台'
admin.site.site_title = 'LYNews--Happy Eary Day'

