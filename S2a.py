# Read the input file
input_file_path = r'C:\ChatGPT\input.txt'  # Update with the correct file path
output_file_path = r'C:\ChatGPT\reversecomplemented.txt'  # Update with the desired output file path

try:
    with open(input_file_path, 'r') as input_file:
        input_string = input_file.read()
except FileNotFoundError:
    print(f"File not found at {input_file_path}. Make sure the file exists.")
    exit(1)

# Reverse the string
reversed_string = input_string[::-1]

# Replace characters according to the rules
complemented_string = ""
for char in reversed_string:
    if char == "A":
        complemented_string += "T"
    elif char == "T":
        complemented_string += "A"
    elif char == "G":
        complemented_string += "C"
    elif char == "C":
        complemented_string += "G"
    else:
        complemented_string += char

# Write the result to the output file
try:
    with open(output_file_path, 'w') as output_file:
        output_file.write(complemented_string)
    print(f"Reverse complemented string saved to {output_file_path}.")
except Exception as e:
    print(f"An error occurred while writing to {output_file_path}: {str(e)}")
