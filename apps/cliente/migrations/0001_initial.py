# Generated by Django 2.2.4 on 2022-10-25 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mantenedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('cod_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('email_cliente', models.EmailField(max_length=255, null=True)),
                ('nombre_cliente', models.CharField(max_length=200)),
                ('apellido_cliente', models.CharField(max_length=200)),
                ('telefono_cliente', models.CharField(max_length=12)),
                ('fecha_reserva', models.DateField(blank=True, null=True, verbose_name='Fecha de la reserva')),
                ('hora_reserva', models.CharField(blank=True, choices=[('14:15', '14:15'), ('15:45', '15:45'), ('13:15', '13:15'), ('15:15', '15:15'), ('15:30', '15:30'), ('16:00', '16:00'), ('13:30', '13:30'), ('14:45', '14:45'), ('13:00', '13:00'), ('15:00', '15:00'), ('16:45', '16:45'), ('14:30', '14:30'), ('16:15', '16:15'), ('14:00', '14:00'), ('16:30', '16:30'), ('13:45', '13:45')], max_length=5, null=True, verbose_name='Hora de la reserva')),
                ('numero_mesa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mantenedor.Mesa')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'ordering': ['cod_reserva'],
            },
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_a_pagar', models.CharField(max_length=6, verbose_name='Total a pagar')),
                ('fecha_de_pago', models.DateField(verbose_name='Fecha de pago')),
                ('estado', models.CharField(blank=True, choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado')], max_length=12, null=True, verbose_name='Estado de pago')),
                ('nombre_apellido_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email', to='cliente.Reserva')),
            ],
            options={
                'verbose_name': 'Boleta',
                'verbose_name_plural': 'Boletas',
                'ordering': ['total_a_pagar'],
            },
        ),
    ]
