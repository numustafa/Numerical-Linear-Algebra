'''The density of a substance is defined as % D=m/V , where m is the mass of a volume
V . Compute and print out the mass of one liter of each of the following substances
whose densities in g/cm3 are found in the file src/files/densities.dat6: iron,
air, gasoline, ice, the human body, silver, and platinum.
'''

densities = {
    "air": 0.0012,
    "gasoline": 0.67,
    "ice": 0.9,
    "pure water": 1.0,
    "seawater": 1.025,
    "human body": 1.03,
    "limestone": 2.6,
    "granite": 2.7,
    "iron": 7.8,
    "silver": 10.5,
    "mercury": 13.6,
    "gold": 18.9,
    "platinium": 21.4,
    "Earth mean": 5.52,
    "Earth core": 13,
    "Moon": 3.3,
    "Sun mean": 1.4,
    "Sun core": 160,
    "proton": 2.3e14
}

def mass_of_one_liter(density: float) -> float:
    """
    Calculate the mass of one liter of a substance given its density.

    Parameters:
    density (float): Density in g/cm^3.

    Returns:
    float: Mass in grams.
    """
    volume = 1000  # 1 liter = 1000 cm^3
    mass = density * volume
    return mass

for substance, density in densities.items():
    mass = mass_of_one_liter(density)
    print(f"The mass of one liter of {substance} is {mass:.1f} grams.")

