# Generated by Django 5.0.4 on 2024-04-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_date_enrolled'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
