def convert_celsius_to_fahrenheit(c):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Args:
        c (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    f = c * (9/5) + 32
    return f


# Get input from user
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

print(f"A text with an integer {2:d} and a float {2.5:f}")



