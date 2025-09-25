# Assignment: File Read/Write and Error Handling

def process_file(input_filename, output_filename):
    """
    Reads content from an input file, adds line numbers, and writes to an output file.
    Handles potential file-related errors.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """
    try:
        # Use 'with' statement for automatic file closing
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            # Enumerate provides a counter (line_num) starting from 1
            for line_num, line in enumerate(infile, 1):
                # Write the line number and the original line content to the new file
                outfile.write(f"{line_num}: {line}")

    except FileNotFoundError:
        # Handle the case where the input file does not exist
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please check the filename and try again.")

    except PermissionError:
        # Handle cases where the script lacks permissions to read or write
        print(f"\nError: Permission denied. Unable to read '{input_filename}' or write to '{output_filename}'.")

    except Exception as e:
        # Catch any other unexpected errors during file processing
        print(f"\nAn unexpected error occurred: {e}")

    else:
        # This block runs only if the 'try' block completes without errors
        print(f"\nSuccess! File '{input_filename}' has been processed and saved as '{output_filename}'.")

# --- Main part of the script ---
if __name__ == "__main__":
    in_file = input("Enter the name of the file to read: ")
    out_file = input("Enter the name for the new, modified file: ")
    process_file(in_file, out_file)

