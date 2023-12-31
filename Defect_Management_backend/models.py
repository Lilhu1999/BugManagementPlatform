from django.db import models
import time


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
    desc = models.CharField(max_length=512, verbose_name='复现步骤')
    iteration = models.CharField(max_length=32, verbose_name='迭代', null=True)
    importance = models.CharField(max_length=16, verbose_name='严重程度')  # 严重程度：致命/严重/一般/建议
    priority = models.CharField(max_length=16, verbose_name='优先级')  # 优先级：紧急/高/中/低
    createTime = models.CharField(max_length=64, verbose_name='创建时间',
                                  default=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    creator = models.CharField(max_length=16, verbose_name='创建人')
    handler = models.CharField(max_length=16, verbose_name='处理人')
    state = models.CharField(max_length=16, verbose_name='缺陷状态', default='待修复')  # 状态：待修复/已修复/重新打开/关闭
    videoPath = models.CharField(max_length=256, verbose_name='视频路径')
    imagePath = models.CharField(max_length=256, verbose_name='图片路径')
    linkId = models.CharField(max_length=8, verbose_name='绑定用例ID', null=True)


# 需求表
class Requirement(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    priority = models.CharField(max_length=16, verbose_name='优先级')  # 紧急/高/中/低
    iteration = models.CharField(max_length=32, verbose_name='迭代名')  # 暂时写死了
    iterationId = models.CharField(max_length=16, verbose_name='迭代id', null=True)
    state = models.CharField(max_length=32, verbose_name='状态', default='进行中')
    handler = models.CharField(max_length=32, verbose_name='处理人')
    start = models.CharField(max_length=32, verbose_name='预计开始')
    end = models.CharField(max_length=32, verbose_name='预计结束')
    desc = models.CharField(max_length=256, verbose_name='需求描述')
    pid = models.CharField(max_length=16, verbose_name='所属项目ID')


# 用例表
class TestCase(models.Model):
    title = models.CharField(max_length=64, verbose_name='标题')
    type = models.CharField(max_length=16, verbose_name='用例类型')
    level = models.CharField(max_length=16, verbose_name='用例等级', null=True)  # 高/中/低
    state = models.CharField(max_length=32, verbose_name='用例状态', default='正常')
    creator = models.CharField(max_length=32, verbose_name='创建人')
    createTime = models.CharField(max_length=64, verbose_name='创建时间',
                                  default=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    desc = models.CharField(max_length=256, verbose_name='用例步骤')
    pid = models.CharField(max_length=16, verbose_name='所属项目ID')
    linkId = models.CharField(max_length=8, verbose_name='绑定需求ID', null=True)


# 迭代表
class Iteration(models.Model):
    title = models.CharField(max_length=32, verbose_name='标题')
    state = models.CharField(max_length=16, verbose_name='状态', default='打开')
    start = models.CharField(max_length=64, verbose_name='开始时间')
    end = models.CharField(max_length=64, verbose_name='结束时间')
    pid = models.CharField(max_length=16, verbose_name='所属项目ID')


# 项目文件表
class ProjectFile(models.Model):
    fileName = models.CharField(max_length=64, verbose_name='文件名')
    filePath = models.CharField(max_length=256, verbose_name='文件路径')
    creator = models.CharField(max_length=64, verbose_name='上传人')
    createTime = models.CharField(max_length=64, verbose_name='创建时间',
                                  default=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
    pid = models.CharField(max_length=16, verbose_name='所属项目ID', null=True)
    document_type = models.CharField(max_length=32, verbose_name='文档类型', null=True)
