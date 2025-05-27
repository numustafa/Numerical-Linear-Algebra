# for loop

degrees = [0, 10, 20, 40, 100]
i = 0
for degree in degrees:
    print(f'{i} list element: {degree}')
    i += 1
print(f'The list has {len(degrees)} elements')

print(f'--------------------------------For Loop---------------------------------------------------')
# program - 2

from Celsius_Fahrenheit_Conversion import convert_celsius_to_fahrenheit
Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
i = 0
for Cdegree in Cdegrees:
    F = convert_celsius_to_fahrenheit(Cdegree)
    print(f'{i} => {Cdegree} Celsius = {F} Fahrenheit')
    i += 1
print(f'The list has {len(Cdegrees)} elements')

print(f'---------------------------------While Loop---------------------------------------------------')

# program - 3 (converting for loop into a while loop)
i = 0                     # index variable
while i < len(Cdegrees):
    Cdegree = Cdegrees[i]
    F = convert_celsius_to_fahrenheit(Cdegree)
    print(f'{i} => {Cdegree} Celsius = {F} Fahrenheit')
    i += 1

print(f'The list has {len(Cdegrees)} elements')

print(f'-------------------------------Replace List with range----------------------------------------------------')

# program - 4 (using range(start, stop, step) to replace list)
for i in range(-20,45,5):
    F = convert_celsius_to_fahrenheit(i)
    print(f'{i} Celsius = {F} Fahrenheit')

print(f'--------------------------------------------------------------------------------------------')
