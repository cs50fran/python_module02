def water_plants(plant_list: list[str]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise TypeError("Cannot water none - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():

    good_list: list = ["tomato", "lettuce", "carrots"]
    bad_list: list = ["tomato", None, "carrots"]

    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(good_list)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(bad_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
