import numpy as np

factorial_5 = np.math.factorial(5)
print(factorial_5)
# Output: 120

# writing a function that calculates sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ... that includes while loop

def sin_approximation(x, max_pwr=25, sign = 1.0):
    """
    Calculate the sine of x using Taylor series approximation.
    
    Args:
        x (float): The angle in radians.
        max_pwr (int): The maximum power to calculate in the series.
        sign (float): The sign of the term, used for alternating series.
        
    Returns:
        float: The approximate value of sin(x).
    """
    k = 1
    while k<=max_pwr:
        k = k+1
        sign = -sign    # alternating sign for the series
        term = sign * (x**k) / np.math.factorial(k)
        sin_x = x + term
        print(f"Term {k}: {term:.16f}, Current sin(x): {sin_x:.16f}")
    return sin_x

if __name__ == "__main__":
    x = float(input("Enter the angle in radians: "))
    sin_x = sin_approximation(x)
    print(f"The approximate value of sin({x}) is: {sin_x:.16f}")
    
    

