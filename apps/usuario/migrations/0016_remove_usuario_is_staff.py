# Generated by Django 2.2.4 on 2022-11-21 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0015_auto_20221120_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='is_staff',
        ),
    ]