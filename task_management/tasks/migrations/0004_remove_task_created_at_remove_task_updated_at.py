# Generated by Django 5.0.6 on 2024-07-07 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_owner_alter_task_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='updated_at',
        ),
    ]
