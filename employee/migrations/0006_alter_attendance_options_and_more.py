# Generated by Django 5.0.4 on 2024-04-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_classroom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-check_in']},
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]