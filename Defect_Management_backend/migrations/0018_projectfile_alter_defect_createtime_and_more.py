# Generated by Django 4.2.3 on 2023-11-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Defect_Management_backend', '0017_remove_requirement_connectioncase_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=64, verbose_name='文件名')),
                ('filePath', models.CharField(max_length=256, verbose_name='文件路径')),
                ('creator', models.CharField(max_length=64, verbose_name='上传人')),
                ('createTime', models.CharField(default='2023-11-10 07:50:49', max_length=64, verbose_name='创建时间')),
                ('pid', models.CharField(max_length=16, verbose_name='所属项目ID')),
            ],
        ),
        migrations.AlterField(
            model_name='defect',
            name='createTime',
            field=models.CharField(default='2023-11-10 07:50:49', max_length=64, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='createTime',
            field=models.CharField(default='2023-11-10 07:50:49', max_length=64, verbose_name='创建时间'),
        ),
    ]
