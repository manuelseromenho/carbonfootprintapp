from django.db import models


class CarbonFootprint(models.Model):
    car_mileage = models.FloatField(null=True, blank=True)
    car_fuel_type = models.CharField(
        max_length=20,
        choices=[
            ("petrol", "Petrol"),
            ("diesel", "Diesel"),
            ("hybrid", "Hybrid"),
        ],
        null=True,
        blank=True,
    )
    motorbike_mileage = models.FloatField(null=True, blank=True)
    motorbike_engine_size = models.IntegerField(null=True, blank=True)  # cc
    electricity_consumption = models.FloatField(null=True, blank=True)  # kWh
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carbon Footprint - {self.created_at}"
