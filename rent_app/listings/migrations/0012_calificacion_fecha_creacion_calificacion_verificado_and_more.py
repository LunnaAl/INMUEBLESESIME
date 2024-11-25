# Generated by Django 5.1.3 on 2024-11-25 03:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0011_reserva_delete_historialrenta"),
    ]

    operations = [
        migrations.AddField(
            model_name="calificacion",
            name="fecha_creacion",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="calificacion",
            name="verificado",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="calificacion",
            name="fecha_fin",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="calificacion",
            name="fecha_inicio",
            field=models.DateField(blank=True, null=True),
        ),
    ]
