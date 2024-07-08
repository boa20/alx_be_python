FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    to_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {to_celsius}°C") 

def convert_to_fahrenheit(celsius):
    to_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {to_fahrenheit}°F") 
    
temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if type(temperature) == float and type(unit) == str:
    if unit == 'C':
        convert_to_fahrenheit(temperature)
    elif unit == 'F':
        convert_to_celsius(temperature)
    else:
        print(f"'{unit}' is an invalid unit.")

else:
    print(f"Invalid temperature. Please enter a numeric value.")


