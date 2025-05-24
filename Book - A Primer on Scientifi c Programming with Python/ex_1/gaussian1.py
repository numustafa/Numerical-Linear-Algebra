'''
Gausian fn is one of the most widely used functions in science and technology. The parameters
m and s > 0 are prescribed real numbers. Make a program for evaluating this
function when m D 0, s D 2, and x D 1. Verify the program’s result by comparing
with hand calculations on a calculator.
'''

import numpy as np

def gausian_fn(x: float, m: float = 0, s: float = 2) -> float:
    """
    Calculate the Gaussian function value for given x, mean (m), and standard deviation (s).

    Parameters:
    x (float): The input value.
    m (float): The mean of the Gaussian function.
    s (float): The standard deviation of the Gaussian function.

    Returns:
    float: The value of the Gaussian function at x.
    """
    gaus_formula = (1/s*np.sqrt(2*np.pi)) * np.exp(-0.5*((x-m)/s)**2)
    return gaus_formula

def main():
    """
    Main function to execute the program.
    """
    try:
        x = float(input("Enter the value of x: "))
        m = float(input("Enter the mean (m): "))
        s = float(input("Enter the standard deviation (s): "))

        if s <= 0:
            print("Standard deviation must be greater than 0.")
            return
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    result = gausian_fn(x, m, s)
    print(f"The value of the Gaussian function at x={x}, m={m}, and s={s} is: {result:.5f}") 
    

if __name__ == "__main__":
    main()
    