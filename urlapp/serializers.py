from rest_framework import serializers

from .models import *
from .url_main import main


class URLSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    short_url = serializers.CharField(read_only=True)

    def create(self, validated_data):
        """
        重写create方法 为了加密密码
        """
        # 调用父类的创建方法
        obj = super(URLSerializer, self).create(validated_data=validated_data)
        obj.short_url = main(validated_data['long_url'])
        obj.save()
        return obj

    class Meta:
        model = URL
        fields = "__all__"
