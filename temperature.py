#Kevin Lashley
#October 19 2025
#Python 115



def main():
    """
    Main function to run the temperature conversion program.
    """
    print("Welcome to the Temperature Converter program, created by [Kevin Lashley]!")

    try:
        flt_temp_value = float(input("Please enter a temperature (e.g., 68.5): "))
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return

    str_temp_unit = input("Is the temperature in Fahrenheit (F) or Celsius (C)? ").strip().upper()

    if str_temp_unit not in ['F', 'C']:
        print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")
        return

    if str_temp_unit == 'F':
        if flt_temp_value < -459.67 or flt_temp_value > 212:
            print("Temperature in Fahrenheit must be between -459.67 and 212.")
        else:
            flt_celsius_equivalent = (5.0 / 9) * (flt_temp_value - 32)
            print(f"The Celsius equivalent is: {flt_celsius_equivalent:.1f}")

    elif str_temp_unit == 'C':
        if flt_temp_value < -273.15 or flt_temp_value > 100:
            print("Temperature in Celsius must be between -273.15 and 100.")
        else:
            flt_fahrenheit_equivalent = ((9.0 / 5.0) * flt_temp_value) + 32
            print(f"The Fahrenheit equivalent is: {flt_fahrenheit_equivalent:.1f}")

if __name__ == "__main__":
    main()
