# Define the file paths
input_file_path = r'C:\CHATGPTclass\tobecleaned.txt'
output_file_path = r'C:\CHATGPTclass\FreshlyLaundered.txt'

# Define the set of allowed characters
allowed_characters = set("ctagu")

# Read the input file and filter the characters
filtered_characters = []
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        for char in line:
            if char.lower() in allowed_characters:
                filtered_characters.append(char)

# Combine the filtered characters into a single string
filtered_string = ''.join(filtered_characters)

# Write the resulting string to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(filtered_string)

print("Filtered string has been saved to", output_file_path)
