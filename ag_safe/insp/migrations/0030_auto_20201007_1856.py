# Generated by Django 3.1 on 2020-10-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0029_auto_20201007_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awpform',
            name='unit_type',
            field=models.TextField(blank=True, null=True),
        ),
    ]
