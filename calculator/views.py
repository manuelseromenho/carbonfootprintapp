import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from .services import calculate_emissions


@ensure_csrf_cookie
def home(request):
    return render(request, "calculator/home.html")


@ensure_csrf_cookie
@require_http_methods(["POST"])
def calculate(request):
    try:
        if request.content_type == "application/json":
            data = json.loads(request.body)
        else:
            data = request.POST

        car_emissions = calculate_emissions.calculate_car_emissions(
            car_mileage=float(data.get("car_mileage", 0)),
            car_fuel_type=data.get("car_fuel_type", "petrol"),
        )

        motorbike_emissions = calculate_emissions.calculate_motorbike_emissions(
            motorbike_mileage=float(data.get("motorbike_mileage", 0)),
            motorbike_engine_size=float(data.get("motorbike_engine_size", 0)),
        )

        electricity_emissions = calculate_emissions.calculate_electricity_emissions(
            electricity_consumption=float(data.get("electricity_consumption", 0))
        )

        total_emissions = car_emissions + motorbike_emissions + electricity_emissions

        results = {
            "car_emissions": car_emissions,
            "motorbike_emissions": motorbike_emissions,
            "electricity_emissions": electricity_emissions,
            "total_emissions": total_emissions,
        }

        if request.content_type == "application/json":
            return JsonResponse(results)
        else:
            return render(request, "calculator/home.html", {"results": results})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
