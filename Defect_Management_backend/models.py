from django.db import models


# Create your models here.
# 部门表
class Department(models.Model):
    name = models.CharField(max_length=64, verbose_name='部门名称')
    parentId = models.IntegerField(verbose_name='上级部门ID', default=0)
    hasChildren = models.CharField(max_length=256, verbose_name='是否有下级部门', null=True)


# 员工表
class Employee(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    password = models.CharField(max_length=32, verbose_name='密码', default='123456')
    deptId = models.CharField(max_length=32, verbose_name='所属部门')
    # type 0:普通用户 1:管理员
    type = models.IntegerField(verbose_name='类型身份', default=0)


# 项目表
class Project(models.Model):
    name = models.CharField(max_length=32, verbose_name='项目名称')
    desc = models.CharField(max_length=128, verbose_name='项目描述')
    dept = models.CharField(max_length=32, verbose_name='项目部门')
    member = models.CharField(max_length=256, verbose_name='项目成员')
    # status 进行中/已完成
    status = models.CharField(max_length=16, verbose_name='项目状态')
    createTime = models.DateField(verbose_name='创建时间')


# 缺陷表
class Defect(models.Model):
    pid = models.CharField(max_length=12, verbose_name='所属项目ID', null=True)
    title = models.CharField(max_length=64, verbose_name='缺陷标题')
    debug = models.CharField(max_length=512, verbose_name='复现步骤')
    belong = models.CharField(max_length=8, verbose_name='所属项目')
    # 严重程度：致命/严重/一般/建议
    importance = models.CharField(max_length=16, verbose_name='严重程度')
    # 优先级：紧急/高/中/低
    priority = models.CharField(max_length=16, verbose_name='优先级')
    createTime = models.DateField(verbose_name='创建时间')
    createPerson = models.CharField(max_length=16, verbose_name='创建人')
    dealPerson = models.CharField(max_length=16, verbose_name='处理人')
    # 状态：待修复/已修复/重新打开/关闭
    status = models.CharField(max_length=16, verbose_name='缺陷状态')
    videoPath = models.CharField(max_length=256, verbose_name='视频路径')
    imagePath = models.CharField(max_length=256, verbose_name='图片路径')


# 需求表
class Requirement(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    priority = models.CharField(max_length=16, verbose_name='优先级')
    iteration = models.CharField(max_length=32, verbose_name='迭代')
    state = models.CharField(max_length=32, verbose_name='状态', default='进行中')
    handler = models.CharField(max_length=32, verbose_name='处理人')
    start = models.CharField(max_length=32, verbose_name='预计开始')
    end = models.CharField(max_length=32, verbose_name='预计结束')
    desc = models.CharField(max_length=256, verbose_name='需求描述')
    pid = models.CharField(max_length=16, verbose_name='所属项目ID')
