def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> str:
    """Check if plant conditions are valid."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    return f"Plant '{plant_name}' is healthy!"

def test_plants_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        result1 = check_plant_health("tomato", 5, 8)
        print(result1)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting empty plant name...")
    try:
        result2 = check_plant_health("", 25, 8)
        print(result2)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad water level values...")
    try:
        result3 = check_plant_health("tomato", 25, 6)
        print(result3)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad sunlight hours...")
    try:
        result3 = check_plant_health("tomato", 5, 0)
        print(result3)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")

if __name__ == "__main__":
    test_plants_checks()