# Create your models here.

from datetime import datetime

from django.db import models


class URL(models.Model):
    long_url = models.CharField(default="",  max_length=1000, verbose_name="长网址", help_text="长网址")
    short_url = models.CharField(default="", max_length=100, verbose_name="短网址", help_text="短网址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "URL集合"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.short_url
