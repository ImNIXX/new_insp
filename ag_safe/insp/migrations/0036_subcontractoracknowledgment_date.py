# Generated by Django 3.1 on 2020-10-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0035_auto_20201019_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcontractoracknowledgment',
            name='date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
