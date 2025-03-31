import pandas as pd

def read_from_console():
    """Reads text from the console."""
    return input("Enter text: ")

def read_from_file_builtin(filepath):
    """Reads text from a file using built-in Python functionality."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None

def read_from_file_pandas(filepath):
    """Reads text from a file using the pandas library."""
    try:
        df = pd.read_csv(filepath, header=None)
        return df.to_string(index=False, header=False)
    except FileNotFoundError:
        print("File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty.")
        return None