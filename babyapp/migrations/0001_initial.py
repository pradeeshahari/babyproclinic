# Generated by Django 5.0 on 2023-12-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adddoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(db_column='user', null=True)),
                ('password', models.TextField(db_column='pass', null=True)),
                ('roll_no', models.PositiveIntegerField(db_column='roll_no', null=True)),
                ('name', models.TextField(db_column='name', null=True)),
                ('age', models.TextField(db_column='age', null=True)),
                ('gender', models.TextField(db_column='gen', null=True)),
                ('number', models.TextField(db_column='number', null=True)),
            ],
        ),
    ]
