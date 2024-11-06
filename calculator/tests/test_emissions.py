import pytest
from django.urls import reverse

from calculator.services import calculate_emissions


@pytest.mark.django_db
class TestEmissionsCalculation:
    def test_car_emissions_calculation(self):
        input_data = {
            "car_mileage": 100.0,
            "car_fuel_type": "petrol",
        }

        emissions = calculate_emissions.calculate_car_emissions(**input_data)
        expected_emission = 2.94

        assert abs(emissions - expected_emission) < 0.01

    def test_motorbike_emissions_calculation(self):
        input_data = {"motorbike_mileage": 50.0, "motorbike_engine_size": 250}

        emissions = calculate_emissions.calculate_motorbike_emissions(**input_data)
        expected_emission = 1.47

        assert abs(emissions - expected_emission) < 0.01

    def test_electricity_emissions_calculation(self):
        consumption = 100
        emissions = calculate_emissions.calculate_electricity_emissions(consumption)
        expected_emission = 25.0

        assert pytest.approx(emissions) == expected_emission


@pytest.mark.django_db
class TestCarbonFootprintViews:
    def test_emissions_summary_calculation(self, client):
        form_data = {
            "car_mileage": 100.0,
            "car_fuel_type": "petrol",
            "motorbike_mileage": 50.0,
            "motorbike_engine_size": 250,
            "electricity_consumption": 200.0,
        }

        response = client.post(reverse("calculator:calculate"), data=form_data)
        result = response.context["results"]

        assert "car_emissions" in result
        assert "motorbike_emissions" in result
        assert "electricity_emissions" in result
        assert "total_emissions" in result

        assert response.status_code == 200

        if "results" in response.context:
            results = response.context["results"]
            assert abs(results["car_emissions"] - 2.94) < 0.01
            assert abs(results["motorbike_emissions"] - 1.47) < 0.01
            assert abs(results["electricity_emissions"] - 50.0) < 0.01
            assert abs(results["total_emissions"] - 54.41) < 0.01


class TestEmissionsValidation:
    def test_negative_values_raise_error(self):
        with pytest.raises(ValueError, match="Mileage cannot be negative"):
            calculate_emissions.calculate_car_emissions(
                car_mileage=-100.0, car_fuel_type="petrol"
            )

    def test_invalid_fuel_type_raises_error(self):
        with pytest.raises(ValueError, match="Invalid fuel type"):
            calculate_emissions.calculate_car_emissions(
                car_mileage=100.0, car_fuel_type="invalid_fuel"
            )
