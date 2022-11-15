# Generated by Django 2.2.4 on 2022-11-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0012_auto_20221115_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='hora_reserva',
            field=models.CharField(blank=True, choices=[('13:00', '13:00'), ('14:15', '14:15'), ('13:30', '13:30'), ('13:15', '13:15'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:15', '15:15'), ('16:15', '16:15'), ('13:45', '13:45'), ('16:00', '16:00'), ('15:30', '15:30'), ('16:30', '16:30'), ('16:45', '16:45'), ('14:00', '14:00'), ('14:45', '14:45'), ('15:45', '15:45')], max_length=5, null=True, verbose_name='Hora de la reserva'),
        ),
    ]