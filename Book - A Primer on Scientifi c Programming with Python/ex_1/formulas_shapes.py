'''
Type the following program in your editor and execute it. If your program does not
work, check that you have copied the code correctly.

from math import pi
h = 5.0 # height
b = 2.0 # base
r = 1.5 # radius
area_parallelogram = h*b
print ’The area of the parallelogram is %.3f’ % area_parallelogram
area_square = b**2
print ’The area of the square is %g’ % area_square
area_circle = pi*r**2
print ’The area of the circle is %.3f’ % area_circle
volume_cone = 1.0/3*pi*r**2*h
print ’The volume of the cone is %.3f’ % volume_cone
'''

import numpy as np

def area_non_circle(h: float, b: float) -> tuple:
    """
    Calculate the area of a non-circle shape (parallelogram or square).
    
    Parameters:
    h (float): Perpendicular Height of the parallelogram.
    b (float): Base of the parallelogram or side of the square."
    ""
    "Returns:
    float: Area of the parallelogram or square.
    """
    area_parallelogram = h * b
    area_square = b ** 2
    return area_parallelogram, area_square

def area_circle(r: float, h: float) -> float:
    """
    Calculate the area of a circle.
    
    Parameters:
    r (float): Radius of the circle.
    
    Returns:
    float: Area of the circle.
    """
    circle = np.pi * r ** 2
    cone = (1.0 / 3) * np.pi * r ** 2 * h
    return circle, cone

def main():
    """
    Main function to execute the program.
    """
    try:
        h = float(input("Enter the height (h): "))
        b = float(input("Enter the base (b): "))
        r = float(input("Enter the radius (r): "))

        if h <= 0 or b <= 0 or r <= 0:
            print(f"Height, base, and radius must be positive numbers.")
            return
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    circle_area, vol_cone = area_circle(r, h)
    area_parallelogram, area_square = area_non_circle(h, b)
    print(f'The area of the parallelogram is {area_parallelogram:.3f}')
    print(f'The area of the square is {area_square:g}')
    print(f'The area of the circle is {circle_area:.3f}')
    print(f'The volume of the cone is {vol_cone:.3f}')

if __name__ == "__main__":
    main()
