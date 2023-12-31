# Generated by Django 4.2.3 on 2023-11-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Defect_Management_backend', '0019_iteration_alter_defect_createtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='iterationId',
            field=models.CharField(max_length=16, null=True, verbose_name='迭代id'),
        ),
        migrations.AlterField(
            model_name='defect',
            name='createTime',
            field=models.CharField(default='2023-11-24 00:39:26', max_length=64, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='createTime',
            field=models.CharField(default='2023-11-24 00:39:26', max_length=64, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='iteration',
            field=models.CharField(max_length=32, verbose_name='迭代名'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='createTime',
            field=models.CharField(default='2023-11-24 00:39:26', max_length=64, verbose_name='创建时间'),
        ),
    ]
