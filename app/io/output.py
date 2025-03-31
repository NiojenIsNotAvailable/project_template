def write_to_console(text):
    """Prints text to the console."""
    print(text)

def write_to_file_builtin(filepath, text):
    """Writes text to a file using built-in Python functionality."""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")
