# Generated by Django 4.2.3 on 2023-11-01 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Defect_Management_backend', '0013_alter_defect_createtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('type', models.CharField(max_length=16, verbose_name='用例类型')),
                ('state', models.CharField(default='正常', max_length=32, verbose_name='状态')),
                ('creator', models.CharField(max_length=32, verbose_name='创建人')),
                ('createTime', models.CharField(default='2023-11-01 02:55:25', max_length=64, verbose_name='创建时间')),
                ('desc', models.CharField(max_length=256, verbose_name='用例步骤')),
                ('pid', models.CharField(max_length=16, verbose_name='所属项目ID')),
            ],
        ),
        migrations.AlterField(
            model_name='defect',
            name='createTime',
            field=models.CharField(default='2023-11-01 02:55:25', max_length=64, verbose_name='创建时间'),
        ),
    ]