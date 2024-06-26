# Generated by Django 5.0.4 on 2024-04-28 21:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leave',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'employee'}, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(limit_choices_to={'groups__name': 'employee'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leave',
            name='employee',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'employee'}, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]
