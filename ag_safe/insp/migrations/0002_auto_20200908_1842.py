# Generated by Django 3.1 on 2020-09-08 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='facility',
            table='insp_facility',
        ),
        migrations.AlterModelTable(
            name='inspections',
            table='insp_inspection',
        ),
        migrations.AlterModelTable(
            name='type',
            table='insp_type',
        ),
    ]
