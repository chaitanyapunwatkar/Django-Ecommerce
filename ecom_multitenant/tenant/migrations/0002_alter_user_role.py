# Generated by Django 4.2.11 on 2024-04-11 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('administrator', 'Admin'), ('customer', 'Customer'), ('supervisor', 'Supervisor'), ('sales_person', 'Sales Person'), ('samta_admin', 'Samta Admin')], max_length=15),
        ),
    ]
