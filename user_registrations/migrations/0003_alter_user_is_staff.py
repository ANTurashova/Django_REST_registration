# Generated by Django 3.2.5 on 2022-03-21 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registrations', '0002_user_entered_invite_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='staff'),
        ),
    ]