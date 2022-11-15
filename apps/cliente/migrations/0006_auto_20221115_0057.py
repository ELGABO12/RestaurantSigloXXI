# Generated by Django 2.2.4 on 2022-11-15 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_auto_20221115_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='estado',
            field=models.CharField(blank=True, choices=[('Pagado', 'Pagado'), ('Pendiente', 'Pendiente')], max_length=12, null=True, verbose_name='Estado de pago'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_reserva',
            field=models.CharField(blank=True, choices=[('14:00', '14:00'), ('13:00', '13:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('16:30', '16:30'), ('14:15', '14:15'), ('13:45', '13:45'), ('15:30', '15:30'), ('15:45', '15:45'), ('16:45', '16:45'), ('14:30', '14:30'), ('13:30', '13:30'), ('15:15', '15:15'), ('16:15', '16:15'), ('13:15', '13:15'), ('14:45', '14:45')], max_length=5, null=True, verbose_name='Hora de la reserva'),
        ),
    ]
