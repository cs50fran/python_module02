class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sun_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sun_hours = sun_hours

    def check_health(self) -> str:
        """Check if plant conditions are valid."""
        if not self.name:
            raise ValueError("Plant name cannot be empty!")
        if self.water_level > 10:
            raise ValueError(f"Water level {self.water_level} "
                             "is too high (max 10)")
        if self.water_level < 1:
            raise ValueError(f"Water level {self.water_level} "
                             "is too low (min 1)")
        if self.sun_hours > 12:
            raise ValueError(f"Sunlight hours {self.sun_hours} "
                             "is too high (max 12)")
        if self.sun_hours < 2:
            raise ValueError(f"Sunlight hours {self.sun_hours} "
                             "is too low (min 2)")
        return (f"{self.name}: healthy"
                f" (water: {self.water_level}, sun: {self.sun_hours})")


class GardenManager:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        try:
            if not plant.name:
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """Water all plants with cleanup."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        except TypeError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_all_health(self) -> None:
        """Check health of all plants."""
        for plant in self.plants:
            try:
                print(plant.check_health())
            except ValueError as e:
                print(f"Error checking {plant.name}: {e}")

    def test_error_recovery(self) -> None:
        """Demonstrate error recovery using custom exceptions."""
        try:
            raise WaterError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")


def test_garden_management() -> None:
    """Demonstrate the full garden management system."""
    print("=== Garden Management System ===\n")
    manager = GardenManager("My Garden")

    print("Adding plants to garden...")
    manager.add_plant(Plant("tomato", 5, 8))
    manager.add_plant(Plant("lettuce", 3, 6))
    manager.add_plant(Plant("", 5, 8))

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_all_health()

    # lettuce with bad water to show error
    bad_lettuce = Plant("lettuce", 15, 6)
    try:
        print(bad_lettuce.check_health())
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    manager.test_error_recovery()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
