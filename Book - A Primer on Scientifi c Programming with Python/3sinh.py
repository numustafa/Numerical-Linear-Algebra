import numpy as np

def sinh(x):
    """
    Calculate the hyperbolic sine of x"
    """
    y = np.sinh(x)
    return y

x = 2*np.pi
r2 = 0.5*(np.exp(x) - np.exp(-x))
r3 = 0.5*(np.exp(1)**x - np.exp(1)**-x)
print(f"for x: {x} sinh : {sinh(x)}, r2: {r2}, r3: {r3}")
print(f"(with 16 dp) for x: {x:.16f} sinh : {sinh(x):.16f}, r2: {r2:.16f}, r3: {r3:.16f}")

