# Generated by Django 4.2.7 on 2023-11-28 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='patient',
            table='patient_registration',
        ),
    ]
