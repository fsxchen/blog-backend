from datetime import datetime
from django.db import models

# Create your models here.
class DailyThink(models.Model):
    """
    每日思考
    """
    content = models.CharField(max_length=255, verbose_name="内容", help_text="内容")
    author = models.CharField(null=True, blank=True, max_length=25, verbose_name="作者", help_text="作者") 
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="添加时间", help_text="添加时间")
    update_time = models.DateTimeField(null=True, blank=True, verbose_name="修改时间",
                                       help_text="修改时间")