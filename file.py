# Part 1: Create and work with a file (like your original)
file = open("example.txt", "w")
file.write("Hello world\n")
file.close()

file = open("example.txt", "r")
data = file.readline()
print("First line:", data)
file.close()

file = open("example.txt", "a")
file.write("Today is amazing\n")
file.close()

# Part 2: Error handling (what the challenge asked for)
input_filename = input("Enter the filename to read: ").strip()

try:
    file = open(input_filename, "r")
    content = file.read()
    print("\nFile content:")
    print(content)
    
    # Simple modification: add stars around each line
    lines = content.split('\n')
    modified_content = ""
    for line in lines:
        if line.strip():  # Only add non-empty lines
            modified_content += f"⭐ {line} ⭐\n"
    
    # Save modified version
    new_file = open("modified_file.txt", "w")
    new_file.write(modified_content)
    new_file.close()
    
    print("\nModified file saved as 'modified_file.txt'")

except FileNotFoundError:
    print("Error: File not found")

except:
    print("Error: Could not read the file")

finally:
    if 'file' in locals() and not file.closed:
        file.close()
    print("Done!")