# Generated by Django 4.2.3 on 2023-09-19 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Defect_Management_backend', '0004_alter_department_haschildren'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='parentId',
            field=models.IntegerField(default=0, max_length=32, verbose_name='上级部门ID'),
        ),
    ]
