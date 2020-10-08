# Generated by Django 3.1 on 2020-09-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0002_auto_20200908_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompressedGasCylinder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plants_name', models.CharField(blank=True, max_length=50)),
                ('cylinder_colour', models.CharField(blank=True, max_length=5)),
                ('cylinder_correct', models.CharField(blank=True, max_length=5)),
                ('cylinder_hoses', models.CharField(blank=True, max_length=5)),
                ('cylinder_upright', models.CharField(blank=True, max_length=5)),
                ('cylinder_suitable', models.CharField(blank=True, max_length=5)),
                ('cylinder_securing', models.CharField(blank=True, max_length=5)),
                ('cylinder_lifting', models.CharField(blank=True, max_length=5)),
                ('cylinder_appropriate', models.CharField(blank=True, max_length=5)),
                ('cylinder_caps', models.CharField(blank=True, max_length=5)),
                ('cylinder_trolley', models.CharField(blank=True, max_length=5)),
                ('cylinder_restrictions', models.CharField(blank=True, max_length=5)),
                ('cylinder_PPE', models.CharField(blank=True, max_length=5)),
                ('cylinder_fire', models.CharField(blank=True, max_length=5)),
                ('cylinder_emergency', models.CharField(blank=True, max_length=5)),
                ('date', models.CharField(blank=True, max_length=50)),
                ('cylinder_id', models.CharField(blank=True, max_length=50)),
                ('isnp_name', models.CharField(blank=True, max_length=50)),
                ('sign', models.CharField(blank=True, max_length=50)),
                ('inspection_id', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'insp_CompressedGasCylinder',
            },
        ),
        migrations.CreateModel(
            name='DraftTables',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('draft_name', models.CharField(max_length=100)),
                ('table_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'insp_draft_tbl',
            },
        ),
    ]