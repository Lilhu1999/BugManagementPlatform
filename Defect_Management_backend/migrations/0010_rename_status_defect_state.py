# Generated by Django 4.2.3 on 2023-10-31 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Defect_Management_backend', '0009_rename_createperson_defect_creator_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='defect',
            old_name='status',
            new_name='state',
        ),
    ]
