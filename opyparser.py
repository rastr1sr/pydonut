import sys
import unicodedata

def parse_opy_to_python(opy_code):
    """Convert `.opy` code using `{` and `}` for blocks into standard Python code."""
    python_code = []
    indentation_level = 0
    next_indentation_level = 0

    # Split by `S` as a delimiter for new lines
    for line in opy_code.split('S'):
        stripped_line = line.strip()
        if not stripped_line:
            continue  # Ignore empty lines

        while stripped_line.startswith('{'):
            if indentation_level > -1:
                indentation_level += 1
            stripped_line = stripped_line[1:].strip()
        next_indentation_level = indentation_level
        
        while stripped_line.endswith('}'):
            if next_indentation_level > -1:
                next_indentation_level -= 1
            stripped_line = stripped_line[:-1].strip()

        python_code.append('    ' * indentation_level + stripped_line)
        indentation_level = next_indentation_level

    if indentation_level != 0:
        print(" Parsing Error: Mismatched '{' and '}' in .opy file.")
        return
    else:
        return '\n'.join(python_code)



def execute_opy_file(file_path):
    """Parse and execute an `.opy` file."""
    try:
        with open(file_path, 'r') as f:
            opy_code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return

    # Parse opy code into Python code
    python_code = parse_opy_to_python(opy_code)

    # Print and execute the Python code
    print(f"Executing the content of '{file_path}' as Python code:")
    print("-" * 50)
    try:
        exec(python_code, {"__name__": "__main__"})
    except Exception as e:
        print(f"Error executing Python code: {e}")


if __name__ == "__main__":
    # Ensure at least one .opy file is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python opy_runner.py <file1.opy> [file2.opy] ...")
        sys.exit(1)

    # Process each .opy file provided as an argument
    for opy_file in sys.argv[1:]:
        if not opy_file.endswith('.opy'):
            print(f"Skipping '{opy_file}': Not an .opy file.")
            continue
        execute_opy_file(opy_file)
