from app.io.output import write_to_console, write_to_file_builtin
from app.io.input import read_from_console, read_from_file_builtin, read_from_file_pandas



def main():
    """Main function that reads text and processes output."""
    console_text = read_from_console()
    file_text_builtin = read_from_file_builtin("input.txt")
    file_text_pandas = read_from_file_pandas("input.csv")

    # Print to console
    write_to_console("Console input:")
    write_to_console(console_text)

    write_to_console("\nFile input (builtin):")
    write_to_console(file_text_builtin if file_text_builtin else "No data.")

    write_to_console("\nFile input (pandas):")
    write_to_console(file_text_pandas if file_text_pandas else "No data.")

    # Write to file
    output_text = f"Console input:\n{console_text}\n\nFile input (builtin):\n{file_text_builtin}\n\nFile input (pandas):\n{file_text_pandas}"
    write_to_file_builtin("output.txt", output_text)


if __name__ == "__main__":
    main()
