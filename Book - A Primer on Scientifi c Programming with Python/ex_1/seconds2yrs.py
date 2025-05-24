''''Can a newborn baby in Norway expect to live for one billion (10^9) seconds? Write
a Python program for doing arithmetics to answer the question.'''''

def can_live_for_one_billion_seconds(life_expectancy_in_yrs: float) -> (int, bool):
    """
    Check if a newborn baby in Norway can expect to live for one billion seconds.

    Parameters:
    life_expectancy_in_yrs (float): The average life expectancy in Norway in years.

    Returns:
    tuple: A tuple containing the number of seconds of avg life expectancy and a boolean indicating if it is greater than one billion seconds.
    """
    seconds_in_a_year = 365.25 * 24 * 60 * 60  # Average seconds in a year considering leap years
    life_expectancy_in_seconds = int(life_expectancy_in_yrs * seconds_in_a_year)
    billion_seconds = 10**9  # One billion seconds
    return life_expectancy_in_seconds, life_expectancy_in_seconds > billion_seconds

def main():
    """
    Main function to get user input, calc life expectency and execute the program.
    """
    try:
        x = float(input("Enter the average life expectancy in Norway (in years): "))
        if x <= 0:
            print("Life expectancy must be a positive number.")
            return
    except ValueError:
        print(f"Invalid input: {e}")
        return
    
    life_expectancy_in_seconds, is_greater = can_live_for_one_billion_seconds(x)
    print(f"The average life expectancy in Norway is {life_expectancy_in_seconds:,} seconds.")
    if is_greater:
        print("A newborn baby in Norway can expect to live for one billion seconds.")
    else:
        print("A newborn baby in Norway cannot expect to live for one billion seconds.")

if __name__ == "__main__":
    main()

    
