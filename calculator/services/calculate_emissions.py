EMISSION_FACTORS = {"petrol": 2.94, "diesel": 2.68, "hybrid": 1.81, "electricity": 0.25}


def calculate_car_emissions(car_mileage, car_fuel_type):
    if car_mileage < 0:
        raise ValueError("Mileage cannot be negative")

    if car_fuel_type not in EMISSION_FACTORS:
        raise ValueError("Invalid fuel type")

    # Calculate emissions using mileage and emission factor
    # Emission factors are in kg CO2 per 100 miles, so divide by 100
    emissions = (car_mileage * EMISSION_FACTORS[car_fuel_type]) / 100.0

    return emissions


def calculate_motorbike_emissions(motorbike_mileage, motorbike_engine_size):
    if motorbike_mileage < 0:
        raise ValueError("Mileage cannot be negative")

    if motorbike_engine_size <= 0:
        raise ValueError("Engine size must be positive")

    emission_factor = EMISSION_FACTORS["petrol"] / 100.0

    return motorbike_mileage * emission_factor


def calculate_electricity_emissions(electricity_consumption):
    if electricity_consumption < 0:
        raise ValueError("Consumption cannot be negative")

    # Using average emission factor (kg CO2/kWh)
    emission_factor = 0.25
    return electricity_consumption * EMISSION_FACTORS["electricity"]
