# Generated by Django 2.0.6 on 2022-08-29 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0014_auto_20220828_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='libro.Autor'),
        ),
    ]
