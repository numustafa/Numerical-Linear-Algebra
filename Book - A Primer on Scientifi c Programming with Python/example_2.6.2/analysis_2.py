# Analyze Algorithm 2.6.2

import matplotlib.pyplot as plt

def compute_monthly_avgs(data):
    """
    Computes the average number of sun hours for each month across all years.
    Returns a list of averages for each month.
    """
    if not data:
        return []
    # Transpose the nested list to group by month
    month_data = list(zip(*data))
    averages = []
    for month in month_data:
        avg = sum(month) / len(month)
        averages.append(avg)
        month_name = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
        print(f"Average sun hours in {month_name[month_data.index(month)]}: {avg:.2f}")
    print("Average sun hours for each month computed successfully.")
    return averages

def find_best_month(averages):
    """
    Determine the month with the maximum average sun hours.
    Returns the name of the month and the maximum average.
    """
    if not averages:
        return None
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    max_avg = max(averages)
    best_month_index = averages.index(max_avg)
    name_of_month = month_names[best_month_index]
    return name_of_month, max_avg


def analyze_decade(data, start_year=1929):
    """
    Analyzes the average sun hours in January and December for each decade.
    Returns a list of tuples with decade labels and their average sun hours.
    """
    if not data:
        return []
    
    # Define decades as tuples of (start_year, end_year, "label")
    decades = [(1930,1939, "1930s"), (1940,1949, "1940s"), (1950,1959, "1950s"),
               (1960,1969, "1960s"), (1970,1979, "1970s"), (1980,1989, "1980s"),
               (1990,1999, "1990s"), (2000,2009, "2000s")]
    # Extract January and December data
    jan_data = [year[0] for year in data]
    dec_data = [year[11] for year in data]
    
    # loop through each data to find decade
    decade_averages = []
    for start, end, label in decades:
        # Get the indices for the decade
        start_index = start - start_year
        end_index = end - start_year + 1
        # loop through each decade to find the average
        dec_jan_vals = []
        for year_index in range(start_index, end_index):
            # add prev yr Dec and current yr Jan
            if year_index > 0 and year_index - 1 < len(dec_data):      # Only add December if the previous year exists
                dec_jan_vals.append(dec_data[year_index - 1])
            if year_index < len(jan_data):                              # Only add January if the current year exists
                dec_jan_vals.append(jan_data[year_index])
        # Calculate the average for January and December
        if dec_jan_vals:
            avg = sum(dec_jan_vals) / (len(dec_jan_vals) * 2*30)
            decade_averages.append((label, avg))
        else:
            decade_averages.append((label, 0.0))
            print(f"Decade: {label}, Average sun hours in January and December: 0.00")
    # Print the results
    for label, avg in decade_averages:
        print(f"Decade: {label}, Average sun hours per day in January and December: {avg:.2f}")
    print("Decade analysis completed successfully.")
    return decade_averages





