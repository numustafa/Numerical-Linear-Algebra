# I am trying to write a while loop, which fetch the F values froom Celsius-Fahrenheit_Conversion.py

# importing function
from Celsius_Fahrenheit_Conversion import convert_celsius_to_fahrenheit

# Initialize the Celsius temperature
c = -5
while c<=40:
    f = convert_celsius_to_fahrenheit(c)
    print(f"{c}°C is equal to {f:.2f}°F")
    # Increment the Celsius temperature by 5
    c += 5


