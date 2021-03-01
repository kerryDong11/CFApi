from rest_framework import serializers
from .models import Student
from .models import User


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student  # 指定的模型类
        fields = ('pk', 'name', 'sex', 'sid',)  # 需要序列化的属性


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('u_account', 'u_id',
                  'u_password',
                  'u_authority',
                  'u_department',
                  'u_name',
                  'is_delete',
                  'u_telephone')
