# Generated by Django 5.0.4 on 2024-04-29 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_leave_reason_alter_attendance_employee_and_more'),
        ('landing', '0001_initial'),
        ('student', '0002_alter_student_date_enrolled'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='landing.course')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.employee')),
                ('students', models.ManyToManyField(blank=True, to='student.student')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]