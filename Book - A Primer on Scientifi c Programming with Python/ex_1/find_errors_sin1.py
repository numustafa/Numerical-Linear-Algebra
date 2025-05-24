'''
Suppose somebody has written a simple one-line program for computing sin.1/:
x=1; print ’sin(%g)=%g’ % (x, sin(x))       -> syntax error also obselete python2 code

Create this program and try to run it. What is the problem?

'''

import numpy as np

def sin(x):
    """
    Calculate the sine of x using numpy.
    """
    return np.sin(x)

def main():
    x = float(input("Enter a value for x: "))
    print(f"sin({x}) = {sin(x)}")

if __name__ == "__main__":
    main()
