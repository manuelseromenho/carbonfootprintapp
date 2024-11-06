from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from .forms import CarbonFootprintForm
from .services import calculate_emissions


@ensure_csrf_cookie
def home(request):
    form = CarbonFootprintForm()
    return render(request, "calculator/home.html", {"form": form})


@require_http_methods(["POST"])
def calculate(request):
    form = CarbonFootprintForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        car_emissions = calculate_emissions.calculate_car_emissions(
            car_mileage=cleaned_data.get("car_mileage", 0),
            car_fuel_type=cleaned_data.get("car_fuel_type", "petrol"),
        )
        motorbike_emissions = calculate_emissions.calculate_motorbike_emissions(
            motorbike_mileage=cleaned_data.get("motorbike_mileage", 0),
            motorbike_engine_size=cleaned_data.get("motorbike_engine_size", 0),
        )
        electricity_emissions = calculate_emissions.calculate_electricity_emissions(
            electricity_consumption=cleaned_data.get("electricity_consumption", 0)
        )
        total_emissions = car_emissions + motorbike_emissions + electricity_emissions

        results = {
            "car_emissions": car_emissions,
            "motorbike_emissions": motorbike_emissions,
            "electricity_emissions": electricity_emissions,
            "total_emissions": total_emissions,
        }
        return render(request, "calculator/results.html", {"results": results})
    else:
        form = CarbonFootprintForm()

    return render(request, "calculator/home.html", {"form": form})
