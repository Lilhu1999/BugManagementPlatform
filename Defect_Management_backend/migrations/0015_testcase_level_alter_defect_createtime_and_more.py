# Generated by Django 4.2.3 on 2023-11-01 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Defect_Management_backend', '0014_testcase_alter_defect_createtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='level',
            field=models.CharField(max_length=16, null=True, verbose_name='用例等级'),
        ),
        migrations.AlterField(
            model_name='defect',
            name='createTime',
            field=models.CharField(default='2023-11-01 02:59:08', max_length=64, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='createTime',
            field=models.CharField(default='2023-11-01 02:59:08', max_length=64, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='state',
            field=models.CharField(default='正常', max_length=32, verbose_name='用例状态'),
        ),
    ]
