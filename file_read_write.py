def read_file(file_name):
    """Read the content of the file and return it."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None
    except IOError:
        print(f"Error: The file '{file_name}' cannot be read.")
        return None

def write_file(file_name, content):
    """Write the modified content to a new file."""
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Modified content has been written to '{file_name}'.")
    except IOError:
        print(f"Error: The file '{file_name}' cannot be written.")

def modify_content(content):
    """Modify the content read from the file."""
    # Example modification: Convert all text to uppercase
    modified_content = content.upper()
    return modified_content

def main():
    input_file = 'input.txt'  # Name of the input file
    content = read_file(input_file)

    if content is not None:
        modified_content = modify_content(content)
        output_file = 'output.txt'  # Name of the output file
        write_file(output_file, modified_content)

if __name__ == "__main__":
    main()