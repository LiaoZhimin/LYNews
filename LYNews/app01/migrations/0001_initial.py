# Generated by Django 2.2.7 on 2021-01-05 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('body', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='摘要')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('category', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='app01.Category', verbose_name='分类')),
                ('tags', models.ManyToManyField(blank=True, to='app01.Tags', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章明细表',
                'verbose_name_plural': '文章明细表',
            },
        ),
    ]
