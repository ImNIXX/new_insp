# Generated by Django 3.1 on 2020-10-06 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0020_confinedspaceentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyExcavation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plants_name', models.CharField(blank=True, max_length=50)),
                ('date', models.CharField(blank=True, max_length=50)),
                ('area', models.CharField(blank=True, max_length=50)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('weather', models.CharField(blank=True, max_length=50)),
                ('rainfall', models.CharField(blank=True, max_length=50)),
                ('authorized', models.CharField(blank=True, max_length=50)),
                ('additional_info', models.CharField(blank=True, max_length=50)),
                ('spoil', models.CharField(blank=True, max_length=5)),
                ('tension', models.CharField(blank=True, max_length=5)),
                ('trench', models.CharField(blank=True, max_length=5)),
                ('seepage', models.CharField(blank=True, max_length=5)),
                ('bracing', models.CharField(blank=True, max_length=5)),
                ('caving', models.CharField(blank=True, max_length=5)),
                ('zones', models.CharField(blank=True, max_length=5)),
                ('egress', models.CharField(blank=True, max_length=5)),
                ('certified', models.CharField(blank=True, max_length=5)),
                ('shoring', models.CharField(blank=True, max_length=5)),
                ('correct', models.CharField(blank=True, max_length=5)),
                ('hydraulic', models.CharField(blank=True, max_length=5)),
                ('adequate', models.CharField(blank=True, max_length=5)),
                ('barricades', models.CharField(blank=True, max_length=5)),
                ('boulders', models.CharField(blank=True, max_length=5)),
                ('vibrations', models.CharField(blank=True, max_length=5)),
                ('safety', models.CharField(blank=True, max_length=5)),
                ('space', models.CharField(blank=True, max_length=5)),
                ('supervisor_name', models.CharField(blank=True, max_length=50)),
                ('sign', models.CharField(blank=True, max_length=50)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insp.inspections')),
            ],
            options={
                'db_table': 'insp_DailyExcavation',
            },
        ),
    ]
