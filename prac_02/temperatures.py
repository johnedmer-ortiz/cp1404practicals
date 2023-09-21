"""
Temperature converter - prac_02
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Displays menu and prompts for user input"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celsius_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def convert_to_fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius"""
    return 5 / 9.0 * (fahrenheit - 32)


main()
