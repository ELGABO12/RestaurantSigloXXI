# Generated by Django 2.2.4 on 2022-11-30 22:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0045_auto_20221130_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenitem',
            name='fecha_orden_item',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_reserva',
            field=models.CharField(blank=True, choices=[('15:45', '15:45'), ('13:30', '13:30'), ('13:15', '13:15'), ('13:45', '13:45'), ('13:00', '13:00'), ('14:15', '14:15'), ('15:00', '15:00'), ('15:30', '15:30'), ('14:00', '14:00'), ('16:00', '16:00'), ('14:30', '14:30'), ('15:15', '15:15'), ('16:30', '16:30'), ('14:45', '14:45'), ('16:15', '16:15'), ('16:45', '16:45')], max_length=5, null=True, verbose_name='Hora de la reserva'),
        ),
    ]
