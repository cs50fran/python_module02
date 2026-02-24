def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        print()

    print("Testing ZeroDivisionError...")
    try:
        5 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        print()

    print("Testing FileNotFoundError...")
    try:
        file = "missing.txt"
        open(file)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        print()

    print("Testing KeyError...")
    try:
        plants: dict[str, str] = {"rose": "red",
                                  "lily": "white",
                                  "daisy": "yellow"}
        cause_error: str = "missing_plant"
        plants[cause_error]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
        print()

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
        print()


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
