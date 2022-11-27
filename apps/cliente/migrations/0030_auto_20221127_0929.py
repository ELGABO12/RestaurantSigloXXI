# Generated by Django 2.2.4 on 2022-11-27 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0013_auto_20221122_0411'),
        ('cliente', '0029_auto_20221127_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='estado',
            field=models.CharField(blank=True, choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado')], max_length=12, null=True, verbose_name='Estado de pago'),
        ),
        migrations.RemoveField(
            model_name='ordenitem',
            name='receta',
        ),
        migrations.AddField(
            model_name='ordenitem',
            name='receta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orden_items', to='mantenedor.Receta'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_reserva',
            field=models.CharField(blank=True, choices=[('15:00', '15:00'), ('16:30', '16:30'), ('13:30', '13:30'), ('14:45', '14:45'), ('15:30', '15:30'), ('16:15', '16:15'), ('16:45', '16:45'), ('13:15', '13:15'), ('15:45', '15:45'), ('13:45', '13:45'), ('14:30', '14:30'), ('15:15', '15:15'), ('14:15', '14:15'), ('16:00', '16:00'), ('13:00', '13:00'), ('14:00', '14:00')], max_length=5, null=True, verbose_name='Hora de la reserva'),
        ),
    ]