# Step 1: Function to read from a file
def read_file(filename):
    with open(filename, "r") as file:
        content = file.read()
    return content


# Step 2: Function to modify the content
def modify_content(content):
    # Example modification: Add stars around each line
    lines = content.split("\n")
    modified = "\n".join([f"* {line} *" for line in lines if line.strip()])
    return modified


# Step 3: Function to write to a new file
def write_file(new_filename, content):
    with open(new_filename, "w") as file:
        file.write(content)


# Step 4: Call the functions in sequence
def main():
    input_filename = input("Enter the filename to read: ").strip()
    try:
        original_content = read_file(input_filename)
        modified_content = modify_content(original_content)

        new_filename = f"modified_{input_filename}"
        write_file(new_filename, modified_content)

        # Step 5: Success message
        print(f"Success! Modified file saved as '{new_filename}'")

    except FileNotFoundError:
        print("Error: File not found")
    except OSError:
        print("Error: Could not read or write the file")


# Run the program
if __name__ == "__main__":
    main()

    
    
