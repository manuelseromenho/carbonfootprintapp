# Generated by Django 5.1.3 on 2024-11-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarbonFootprint",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_mileage", models.FloatField(blank=True, null=True)),
                (
                    "car_fuel_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("petrol", "Petrol"),
                            ("diesel", "Diesel"),
                            ("hybrid", "Hybrid"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("car_efficiency", models.FloatField(blank=True, null=True)),
                ("motorbike_mileage", models.FloatField(blank=True, null=True)),
                ("motorbike_engine_size", models.IntegerField(blank=True, null=True)),
                ("electricity_consumption", models.FloatField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]