# File Access and Data Reader
import ast

def read_sun_hrs_data(filename):
    """
    Reads the .txt sun hours data from a file and returns it as a list of lists.
    Each inner list contains the sun hours for a month across multiple years.
    """
    try:
        with open(filename, 'r') as file:
            data = ast.literal_eval(file.read())
        return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except SyntaxError:
        print(f"Error: The file {filename} contains invalid syntax.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
            
    