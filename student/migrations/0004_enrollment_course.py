# Generated by Django 5.0.4 on 2024-04-29 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
        ('student', '0003_attendance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='landing.course'),
        ),
    ]