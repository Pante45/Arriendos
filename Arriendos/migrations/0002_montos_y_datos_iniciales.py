from datetime import date

from django.db import migrations, models


def crear_datos_iniciales(apps, schema_editor):
    Equipo = apps.get_model("Arriendos", "Equipo")
    Arriendo = apps.get_model("Arriendos", "Arriendo")

    datos_equipos = [
        ("Taladro percutor", "Taladro industrial de 800 W", date(2025, 3, 12), "Disponible", 129900),
        ("Generador portátil", "Generador eléctrico de 3.5 kW", date(2025, 5, 8), "En arriendo", 549900),
        ("Hidrolavadora", "Hidrolavadora de alta presión", date(2025, 8, 21), "Disponible", 289900),
        ("Compactadora de placa", "Compactadora para obras y pavimentos", date(2025, 11, 3), "Mantención", 799900),
    ]
    equipos = {}
    for nombre, descripcion, adquisicion, estado, valor in datos_equipos:
        equipo, _ = Equipo.objects.get_or_create(
            nombre=nombre,
            defaults={
                "descripcion": descripcion,
                "fecha_adquisicion": adquisicion,
                "estado": estado,
                "valor_adquisicion": valor,
            },
        )
        equipos[nombre] = equipo

    datos_arriendos = [
        ("Taladro percutor", "Constructora Norte", date(2026, 9, 2), date(2026, 9, 5), 29990),
        ("Generador portátil", "Eventos del Valle", date(2026, 9, 4), date(2026, 9, 9), 89990),
        ("Taladro percutor", "Marta Rojas", date(2026, 9, 10), date(2026, 9, 12), 24990),
        ("Hidrolavadora", "Servicios Rivera", date(2026, 9, 13), date(2026, 9, 16), 45990),
        ("Generador portátil", "Producciones Sur", date(2026, 9, 18), date(2026, 9, 22), 109990),
        ("Compactadora de placa", "Obras del Parque", date(2026, 9, 23), date(2026, 9, 25), 67990),
    ]
    for nombre_equipo, cliente, inicio, fin, monto in datos_arriendos:
        Arriendo.objects.get_or_create(
            equipo=equipos[nombre_equipo],
            cliente=cliente,
            fecha_inicio=inicio,
            defaults={"fecha_fin": fin, "monto": monto},
        )


class Migration(migrations.Migration):
    dependencies = [("Arriendos", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="equipo",
            name="valor_adquisicion",
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="arriendo",
            name="monto",
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.RunPython(crear_datos_iniciales, migrations.RunPython.noop),
    ]