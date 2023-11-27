# Generated by Django 4.2.3 on 2023-11-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Defect_Management_backend', '0020_requirement_iterationid_alter_defect_createtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='createTime',
            field=models.CharField(default='2023-11-27 05:42:50', max_length=64, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='defect',
            name='state',
            field=models.CharField(default='待修复', max_length=16, verbose_name='缺陷状态'),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='createTime',
            field=models.CharField(default='2023-11-27 05:42:50', max_length=64, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='createTime',
            field=models.CharField(default='2023-11-27 05:42:50', max_length=64, verbose_name='创建时间'),
        ),
    ]