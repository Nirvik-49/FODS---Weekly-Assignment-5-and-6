def copy_file():
    """
    Reads content from a source file and writes to a destination file.
    Handles various file operation exceptions gracefully.
    """
    
    try:
        # Get input and output file names from user
        input_file = input("Enter the name of the input file: ")
        output_file = input("Enter the name of the output file: ")

        # Check if output file already exists
        if os.path.exists(output_file):
            overwrite = input(f"File '{output_file}' already exists. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                print("Operation cancelled by user.")
                return

        # Read from input file
        
        with open(input_file, 'r') as source:
            content = source.read()

        # Write to output file
        
        with open(output_file, 'w') as destination:
            destination.write(content)

        print(f"File copied successfully from '{input_file}' to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' does not exist.")
    except PermissionError:
        print("Error: You don't have permission to access one of these files.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Import needed for os.path.exists

import os

# Run the program
if __name__ == "__main__":
    copy_file()

