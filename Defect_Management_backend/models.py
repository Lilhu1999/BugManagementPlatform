from django.db import models


# Create your models here.
# 部门表
class Department(models.Model):
    name = models.CharField(max_length=64, verbose_name='部门名称')
    parentId = models.CharField(max_length=32, verbose_name='上级部门ID', default='null')
    children = models.CharField(max_length=256, verbose_name='下级部门', default='null')


# 员工表
class Employee(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    password = models.CharField(max_length=32, verbose_name='密码', default='123456')
    deptId = models.CharField(max_length=32, verbose_name='所属部门')
    # type 0:普通用户 1:管理员
    type = models.IntegerField(verbose_name='类型身份', default=0)
