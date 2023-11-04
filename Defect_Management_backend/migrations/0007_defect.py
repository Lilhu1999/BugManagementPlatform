# Generated by Django 4.2.3 on 2023-10-09 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Defect_Management_backend', '0006_project_alter_department_parentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='缺陷标题')),
                ('debug', models.CharField(max_length=512, verbose_name='复现步骤')),
                ('belong', models.CharField(max_length=8, verbose_name='所属项目')),
                ('importance', models.CharField(max_length=16, verbose_name='严重程度')),
                ('priority', models.CharField(max_length=16, verbose_name='优先级')),
                ('createTime', models.DateField(verbose_name='创建时间')),
                ('createPerson', models.CharField(max_length=16, verbose_name='创建人')),
                ('dealPerson', models.CharField(max_length=16, verbose_name='处理人')),
                ('status', models.CharField(max_length=16, verbose_name='缺陷状态')),
                ('videoPath', models.CharField(max_length=256, verbose_name='视频路径')),
                ('imagePath', models.CharField(max_length=256, verbose_name='图片路径')),
            ],
        ),
    ]
