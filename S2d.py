# Define the file paths
input_file_path = r'C:\CHATGPTclass\input.txt'
output_file_path = r'C:\CHATGPTclass\reversecomplemented.txt'

# Read the input file and reverse the order of characters
with open(input_file_path, 'r') as input_file:
    input_string = input_file.read()
    reversed_string = input_string[::-1]

# Replace characters as specified
replacement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
complemented_string = ''.join(replacement_dict.get(char, char) for char in reversed_string)

# Write the resulting string to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(complemented_string)

print("Reverse complemented string has been saved to", output_file_path)
