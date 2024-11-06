from django import forms

from .models import CarbonFootprint


class CarbonFootprintForm(forms.ModelForm):
    class Meta:
        model = CarbonFootprint
        fields = [
            "car_mileage",
            "car_fuel_type",
            "motorbike_mileage",
            "motorbike_engine_size",
            "electricity_consumption",
        ]
        widgets = {
            "car_fuel_type": forms.Select(
                choices=[
                    ("petrol", "Petrol"),
                    ("diesel", "Diesel"),
                    ("hybrid", "Hybrid"),
                ]
            ),
        }
