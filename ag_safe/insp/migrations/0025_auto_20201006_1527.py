# Generated by Django 3.1 on 2020-10-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insp', '0024_earthmovingequipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='access_good',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='access_na',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='access_rejected',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='access_remarks',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='backup_good',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='engine_condition',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='equipment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='equipment_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='equipment_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='other_specify',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='earthmovingequipment',
            name='plants_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='EmergencyEvacuation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plants_name', models.CharField(blank=True, max_length=50, null=True)),
                ('equipment_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('time_drill', models.CharField(blank=True, max_length=50, null=True)),
                ('location_drill', models.TextField(blank=True, null=True)),
                ('des_drill', models.TextField(blank=True, null=True)),
                ('des_deficiencies', models.TextField(blank=True, null=True)),
                ('work_one', models.CharField(blank=True, max_length=50, null=True)),
                ('work_two', models.CharField(blank=True, max_length=50, null=True)),
                ('work_three', models.CharField(blank=True, max_length=50, null=True)),
                ('work_four', models.CharField(blank=True, max_length=50, null=True)),
                ('work_five', models.CharField(blank=True, max_length=50, null=True)),
                ('work_six', models.CharField(blank=True, max_length=50, null=True)),
                ('work_seven', models.CharField(blank=True, max_length=50, null=True)),
                ('work_eight', models.CharField(blank=True, max_length=50, null=True)),
                ('work_nine', models.CharField(blank=True, max_length=50, null=True)),
                ('work_ten', models.CharField(blank=True, max_length=50, null=True)),
                ('work_eleven', models.CharField(blank=True, max_length=50, null=True)),
                ('work_twelve', models.CharField(blank=True, max_length=50, null=True)),
                ('work_thirteen', models.CharField(blank=True, max_length=50, null=True)),
                ('work_fourteen', models.CharField(blank=True, max_length=50, null=True)),
                ('work_fifteen', models.CharField(blank=True, max_length=50, null=True)),
                ('date_last_drill', models.CharField(blank=True, max_length=50, null=True)),
                ('noted_deficiencies', models.TextField(blank=True, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insp.inspections')),
            ],
            options={
                'db_table': 'insp_EmergencyEvacuation',
            },
        ),
    ]