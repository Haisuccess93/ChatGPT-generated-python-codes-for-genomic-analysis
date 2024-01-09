import random
import os

# Define the file paths
input_file_path = r'C:\CHATGPTclass\peak.txt'
output_file_path = r'C:\CHATGPTclass\scrambled.txt'

# Check if the input file exists
if not os.path.exists(input_file_path):
    print("Input file 'peak.txt' not found.")
else:
    # Read the contents of the input file
    with open(input_file_path, 'r') as input_file:
        original_text = input_file.read()

    # Convert the original text into a list of characters
    characters = list(original_text)

    # Shuffle the characters randomly
    random.shuffle(characters)

    # Create the output folder if it doesn't exist
    output_folder = os.path.dirname(output_file_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write the scrambled text to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(''.join(characters))

    print(f"Scrambled text written to '{output_file_path}'")
