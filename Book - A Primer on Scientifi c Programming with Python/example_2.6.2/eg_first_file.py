'''
The oxford_sun_hours.txt2 contains data of the number
of sun hours in Oxford, UK, for every month since January 1929. The data are
already on a suitable nested list format:
The list in every line holds the number of sun hours for each of the year’s 12 months.
That is, the first index in the nested list corresponds to year and the second index
corresponds to the month number. More precisely, the double index [i][j] corresponds
to year 1929 + i and month 1 + j (January being month number 1).
The task is to define this nested list in a program and do the following data
analysis.
'''

import ast
# Accessing .txt file and Data Structure
def read_sun_hrs_file(filename):
    """
    Reads the sun hours data from a text file and returns it as a nested list.
    Each sublist corresponds to a year, with 12 elements for each month's sun hours.
    """
    try:
        with open(filename, 'r') as file:
            data = ast.literal_eval(file.read())
        return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None

# Define the file name
filename = 'oxford_sun_hours.txt'
# Read the data from the file
sun_hours_data = read_sun_hrs_file(filename)
if sun_hours_data is None:
    raise SystemExit("Data could not be loaded. Exiting...")
else:
    print("Data loaded successfully.")

# 1. Compute the mean number of sun hours for each month across all years.
def mean_sun_hrs_zip(data):
    """
    Computes the mean number of sun hours for each month across all years.
    Returns a list of means for each month.
    """
    if not data:
        return []
    month_data = list(zip(*data))  # Transpose the nested list to group by month
    means_list= []
    for month in month_data:
        avg = sum(month) / len(month)
        means_list.append(avg)
        month_name = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
        print(f"Mean sun hours in {month_name[month_data.index(month)]}: {avg:.2f}")
    print("Mean sun hours for each month computed successfully.")

    return means_list

mean_sun_hours = mean_sun_hrs_zip(sun_hours_data)

print(f'----------------------------------------------------------------------------------------------------')
# 2. Which month has the best weather according to the means found in the preceding task?
def best_month_weather(means):
    """
    Determine the month with max mean hrs of sunlight

    """
    if not means:
        return None
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    max_mean = max(means)
    best_month_index = means.index(max_mean)
    name_of_month = month_names[best_month_index]
    print(f"The month with the best weather (with max sunlight hrs) is {name_of_month} with an average of {max_mean:.2f} sun hours.")

    return name_of_month, max_mean
best_month, best_mean = best_month_weather(mean_sun_hours)

print(f'----------------------------------------------------------------------------------------------------')


# 3. For each decade, 1930–1939, 1940–1949, : : :, 2000–2009, compute the average number of sun hours per day in January and December. For example, use December 1949, January 1950, : : :, December 1958, and January 1959 as data for the decade 1950–1959. Are there any noticeable differences between the decades?
    # Define decates as tuples of (start_year, end_year, "label")
def analyze_decades(data, start_year=1929):
    """
    Analyzes the average sun hours in January and December for each decade.
    Returns a list of tuples with decade labels and their average sun hours.
    """
    if not data:
        print("No data available for analysis.")
        return []
    decades = [(1930, 1939, "1930s"), (1940, 1949, "1940s"), (1950, 1959, "1950s"),
               (1960, 1969, "1960s"), (1970, 1979, "1970s"), (1980, 1989, "1980s"),
               (1990, 1999, "1990s"), (2000, 2009, "2000s")]
    # Extract jan and Dec values from data
    jan_values = [year[0] for year in data]
    dec_values = [year[11] for year in data]

    # process each decade
    decade_averages = []
    # Loop through decade
    for start, end, label in decades:
        start_index = start - start_year
        end_index = end - start_year + 1  # +1 to include the last year of the decade
        # Loop through years inside this decade
        winter_months = []
        for year_index in range(start_index, end_index):
            # add dec of previous year
            if year_index > 0:
                winter_months.append(dec_values[year_index - 1])
            # add jan of current year - check if current Jan exists
            if year_index < len(jan_values):
                winter_months.append(jan_values[year_index])
        # Calculate the average for this decade
        if winter_months:
            avg_sun_hours_per_day = sum(winter_months) / (len(winter_months)*30)
            decade_averages.append((label, avg_sun_hours_per_day))
        else:
            decade_averages.append((label, 0))
            print(f"Decade: {label}, Average sun hours in January and December: 0.00")

    # Print the results
    for decade, avg in decade_averages:
        print(f"Decade: {decade}, Average sun hours in January and December per day: {avg:.1f}")
    print("Decade analysis completed successfully.")
    return decade_averages

decade_analysis = analyze_decades(sun_hours_data)

print(f'----------------------------------------------------------------------------------------------------')
                


    
    

