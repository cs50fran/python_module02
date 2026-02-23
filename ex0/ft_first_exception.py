def check_temperature(temp_str: str) -> int | None:
    """Validate a temperature string for plant safety (0-40°C)."""
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return None
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return None

    print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input() -> None:
    """Test temperature validation with various inputs."""
    print("=== Garden Temperature Checker ===")

    test_cases = ["25", "abc", "100", "-50"]

    for temp in test_cases:
        print(f"\nTesting temperature: {temp}")
        check_temperature(temp)

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
