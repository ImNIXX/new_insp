# Generated by Django 3.1 on 2020-10-03 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0006_auto_20201003_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compressedgascylinder',
            old_name='inspection_id',
            new_name='inspection',
        ),
    ]
