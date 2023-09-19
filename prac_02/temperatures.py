

def celsius_to_fahrenheit(celsius):
    """Converts celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius"""
    return 5 / 9.0 * (fahrenheit - 32)

def main():
    """Displays menu and prompts for user input"""
    MENU = "C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()