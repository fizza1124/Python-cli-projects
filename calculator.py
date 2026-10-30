from datetime import datetime
def read_number(prompt):
    """Read a valid number and retry if the input is invalid."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def format_number(number):
    """Display whole numbers without unnecessary decimal places."""
    return str(int(number)) if number.is_integer() else f"{number:.10g}"


def calculate(first, operator, second):
    """Perform the arithmetic operation."""

    if operator == "+":
        return first + second

    elif operator == "-":
        return first - second

    elif operator == "*":
        return first * second

    elif operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second

    elif operator == "%":
        if second == 0:
            raise ZeroDivisionError("Cannot use modulo with zero.")
        return first % second

    elif operator == "**":
        if abs(second) > 1000:
            raise ValueError("Exponent is too large.")
        return first ** second

    else:
        raise ValueError("Unsupported operation.")

def main():
    """Control the calculator application."""
    history = []

    print("Welcome to the Python Calculator!")

    while True:
        operator = input("Choose an operation: ").strip().lower()

        # Exit the application cleanly.
        if operator == "q":
            print("Calculator closed. Goodbye!")
            break

        # Reject unsupported operators before requesting numbers.
        if operator not in {"+", "-", "*", "/", "%", "**"}:
            print("Invalid operation. Please choose a listed operator.")
            continue

        first = read_number("Enter the first number: ")
        second = read_number("Enter the second number: ")

        try:
            result = calculate(first, operator, second)

            expression = (
                f"{format_number(first)} {operator} "
                f"{format_number(second)} = {format_number(result)}"
            )

            print(f"\nResult: {expression}")

            # Timestamp each successful calculation in session history.
            history.append(
                f"{datetime.now():%H:%M:%S} | {expression}"
            )

        except (ValueError, ZeroDivisionError, OverflowError) as error:
            # Report mathematical errors without crashing the program.
            print(f"Calculation error: {error}")


if __name__ == "__main__":
    main()


