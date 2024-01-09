import os
import random

# Define the paths to the input and output files
input_file_path = r'C:\CHATGPTclass\peak.txt'
output_file_path = r'C:\CHATGPTclass\scrambled.txt'

# Check if the input file exists
if not os.path.exists(input_file_path):
    print(f"Input file '{input_file_path}' does not exist.")
else:
    # Read the content from the input file
    with open(input_file_path, 'r') as input_file:
        original_text = input_file.read()

    # Convert the original text into a list of characters
    characters = list(original_text)

    # Shuffle the characters randomly
    random.shuffle(characters)

    # Convert the shuffled characters back to a string
    scrambled_text = ''.join(characters)

    # Write the scrambled text to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(scrambled_text)

    print(f"Scrambled text has been saved to '{output_file_path}'.")
