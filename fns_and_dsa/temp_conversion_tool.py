# 3. Temperature Conversion Tool
# Illustrate the concept of variable scope by creating a script that converts temperatures 
# between Celsius and Fahrenheit, using global variables to store conversion factors.



# The formulas for conversion are:
# C = (F - 32) * (5/9)
# F = (C * (9/5)) + 32
# Note: The factors are stored as floating-point numbers for accurate division.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion Functions

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    C = (F - 32) * (5/9)
    """
    # Accessing the global variable without the 'global' keyword because we are only reading it.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    F = (C * (9/5)) + 32
    """
    # Accessing the global variable without the 'global' keyword because we are only reading it.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main Logic and User Interaction

def main():
    try:
        # Prompt user for temperature and validate that it is a number
        temp_input = input("Enter the temperature to convert: ")
        
        # Attempt to convert input to a float, raising an error if it fails
        temperature = float(temp_input)

        # Prompt user for the unit and normalize the input
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        unit = unit_input.strip().upper()

        if unit == 'F':
            # Convert F to C
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
            
        elif unit == 'C':
            # Convert C to F
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        # Catch the error if float(temp_input) fails (non-numeric input)
        # This addresses the requirement to raise a specific error message for invalid temperature.
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()