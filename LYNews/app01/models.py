from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField('分类',max_length=100)

    class Meta:
        verbose_name = '分类表'
        verbose_name_plural = verbose_name

    def __str__(self):  # 对象显示的信息，表的每行提示的内容
        return self.name
    

class Tags(models.Model):
    name = models.CharField('标签',max_length=100)

    class Meta:
        verbose_name = '标签表'
        verbose_name_plural = verbose_name

    def __str__(self):  # 对象显示的信息，表的每行提示的内容
        return self.name
    

class Article(models.Model):
    """分类"""
    name = models.CharField("名称",max_length=100,null=False)
    # db_index=False 是否为该参数创建索引，默认值：default =， max_length =30 限制字符长度 
    # primary_key = False 主键，一般和AutoField()一起使用，unique=False 是否唯一值
    # sex = models.BooleanField('性别',choices=[(True,'男'),(False,'女'),],default=False) # 布尔字段，值为True或False
    # points = models.DecimalField(max_digits=8, decimal_places=2) # 十进制浮点数，共8位其中2位小数
    # points2= models.FloatField() name,category,tags,excerpt,body,created_time,views,photo
    body = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now=True, auto_now_add=False)
    excerpt = models.CharField('摘要', max_length=200, blank=True)  # 文章摘要，可为空
    # ForeignKey表示1对多（多个post对应1个category）
    # category = models.ForeignKey(Category, on_delete=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', default='1')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='标签')
    views = models.PositiveIntegerField('阅读量',default=0)  # 阅读量
    # photo = models.ImageField('额外图片',null=True, upload_to = 'photos/%Y/%m/%d/')
    
    class Meta:
        verbose_name = '文章明细表'
        verbose_name_plural = verbose_name

    def __str__(self):  # 对象显示的信息，表的每行提示的内容
        return self.name


