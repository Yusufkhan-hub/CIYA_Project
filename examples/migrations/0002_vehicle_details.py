# Generated by Django 2.2.20 on 2021-06-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_actice', models.BooleanField(default=False)),
                ('wheeler', models.IntegerField()),
                ('transporter', models.CharField(max_length=100)),
                ('rc_no', models.CharField(max_length=70)),
                ('chasis_no', models.CharField(max_length=70)),
                ('vehicle_no', models.CharField(max_length=50)),
                ('rfid_tag', models.IntegerField()),
                ('vehicle_temp_no', models.CharField(blank=True, max_length=50, null=True)),
                ('permit_type', models.CharField(blank=True, max_length=50, null=True)),
                ('road_tax', models.CharField(max_length=50)),
                ('fitness', models.CharField(max_length=50)),
                ('insurance', models.CharField(max_length=50)),
                ('pollution', models.CharField(max_length=50)),
                ('permit', models.CharField(max_length=50)),
                ('road_taxt_expriry', models.DateField()),
                ('fitnes_expiry', models.DateField()),
                ('insurance_expiry', models.DateField()),
                ('pollution_expiry', models.DateField()),
                ('permit_expiry', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('vehicle_owner', models.CharField(max_length=50)),
                ('owner_address', models.CharField(max_length=50)),
                ('status_change_date', models.DateField()),
                ('owner_contact', models.IntegerField()),
                ('own_vehivle', models.BooleanField(default=False)),
            ],
        ),
    ]