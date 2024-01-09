import random

# Path to the input file containing the linear string of characters
input_file_path = r"C:\CHATGPTclass\peak.txt"

# Path to the output file for the scrambled characters
output_file_path = r"C:\CHATGPTclass\scrambled.txt"

# Read the linear string of characters from the input file
with open(input_file_path, 'r') as input_file:
    linear_string = input_file.read().strip()

# Scramble the order of characters
scrambled_string = ''.join(random.sample(linear_string, len(linear_string)))

# Write the scrambled string to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(scrambled_string)

print("String scrambled and saved to 'scrambled.txt'.")
