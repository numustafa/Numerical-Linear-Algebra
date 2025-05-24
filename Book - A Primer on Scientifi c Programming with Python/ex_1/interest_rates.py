'''
Make a program for computing how much money 1000 euros have
grown to after three years with 5 percent interest rate.
'''

def accumulation(principal: float, rate: float, yrs:float) -> float:
    """
    Calculate the accumulated amount after a certain number of years with compound interest.

    Parameters:
    principal (float): The initial amount of money.
    rate (float): The interest rate (as a decimal).
    yrs (float): The number of years the money is invested or borrowed for.

    Returns:
    float: The accumulated amount after the specified number of years.
    """
    amount = principal * (1 + (rate/100)) ** yrs
    return amount

def main():
    """
    Main function to execute the program.
    """
    try:
        rate = float(input("Enter interest rate (in % points): "))
        principal_amount = float(input("Enter principal amount (in euros): "))
        years = float(input("Enter number of years: "))
        if rate < 0 or principal_amount < 0 or years < 0:
            print("All values must be non-negative.")
            return
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    accumulation_amount = accumulation(principal_amount, rate, years)
    print(f"Accumulated amount after {years} years at {rate}% interest rate: {accumulation_amount:.2f} euros")


if __name__ == "__main__":
    main()

