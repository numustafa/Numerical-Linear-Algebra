''''Make a program where you set a length given in meters and then compute and write
out the corresponding length measured in inches, in feet, in yards, and in miles. Use
that one inch is 2.54 cm, one foot is 12 inches, one yard is 3 feet, and one British
mile is 1760 yards. For verification, a length of 640 meters corresponds to 25196.85
inches, 2099.74 feet, 699.91 yards, or 0.3977 miles.'''''

def length_conversion(meters: float) -> dict:
    """
    Convert length from meters to inches, feet, yards, and miles.

    Parameters:
    meters (float): Length in meters.

    Returns:
    dict: A dictionary containing the converted lengths.
    """
    inches = meters / 0.0254
    feet = inches / 12
    yards = feet / 3
    miles = yards / 1760

    return {
        "inches": inches,
        "feet": feet,
        "yards": yards,
        "miles": miles
    }

def main():
    """
    Main function to get user input and execute the program.
    """
    try:
        x = float(input("Enter length in meters: "))
        if x < 0:
            print("Length must be a non-negative number.")
            return
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    converted_lengths = length_conversion(x)
    print(f"Length in meters: {x:.2f}")
    print(f"Length in inches: {converted_lengths['inches']:.2f}")
    print(f"Length in feet: {converted_lengths['feet']:.2f}")
    print(f"Length in yards: {converted_lengths['yards']:.2f}")
    print(f"Length in miles: {converted_lengths['miles']:.4f}")


    

if __name__ == "__main__":
    main()
    