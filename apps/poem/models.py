from django.db import models

# Create your models here.

class Poet(models.Model):
    total_num = models.IntegerField(verbose_name="数量", help_text="数量", default=0)
    all = models.IntegerField(verbose_name="数量", help_text="数量", default=0, blank=True, null=True)
    age = models.CharField(verbose_name="年代", max_length=25)
    poet_comment = models.TextField(verbose_name="诗人评价")
    name = models.CharField(max_length=25, verbose_name="名字")
    url = models.CharField(max_length=255, verbose_name="url")
    total_url = models.CharField(max_length=255, verbose_name="url")
    poet_intr = models.TextField(verbose_name="诗人介绍")
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="添加时间", help_text="添加时间")

class Poem(models.Model):
    content = models.TextField(verbose_name="内容")
    age = models.CharField(max_length=25, verbose_name="年代")
    auth = models.ForeignKey(Poet, on_delete=models.DO_NOTHING, blank=True, null=True)
    auth_name = models.CharField(max_length=25, verbose_name="作者")
    url = models.CharField(max_length=255, verbose_name="url")
    categ = models.CharField(max_length=25, verbose_name="类别")
    title = models.CharField(max_length=255, verbose_name="标题")
    comment = models.TextField(verbose_name="评价")
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="添加时间", help_text="添加时间")
