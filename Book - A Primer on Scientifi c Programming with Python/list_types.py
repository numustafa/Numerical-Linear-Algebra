# nested lists
from Celsius_Fahrenheit_Conversion import convert_celsius_to_fahrenheit

print(f'---------------------------------Nested List---------------------------------------------------')
C_degrees = range(-20,41,5)  # Celsius degrees from -20 to 40 with a step of 5
F_degrees = [convert_celsius_to_fahrenheit(Cdegree) for Cdegree in C_degrees]  # Convert to Fahrenheit
table = [C_degrees, F_degrees]  # Create a nested list
print (table)
print("Celsius to Fahrenheit Conversion Table:")
for row in table:
    print(row)
print(f'The table has {len(table)} rows and {len(table[0])} columns')

print(f'---------------------------------Nested List with [C,F]---------------------------------------------------')
new_table = []
for c,f in zip(C_degrees, F_degrees):
    new_table.append([c, f])  # Append a list of [Celsius, Fahrenheit] to the new table
print("Celsius to Fahrenheit Conversion Table with [C,F]:")
for row in new_table:
    print(row)
print(f'The new table has {len(new_table)} rows and {len(new_table[0])} columns')

print(f'---------------------------------Sub-list Operations---------------------------------------------------')
# part of the table list of [C, F] rows (see Sect. 2.4) where the Celsius degrees are between 10 and 35 (not including 35):

for c,f in new_table[C_degrees.index(10):C_degrees.index(35)]:
    print([c, f])  # Print the sub-list of [Celsius, Fahrenheit] for degrees between 10 and 35
print(f'The sub-list has {len(new_table[C_degrees.index(10):C_degrees.index(35)])} rows and {len(new_table[0])} columns')
