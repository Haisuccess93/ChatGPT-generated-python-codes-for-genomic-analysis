import random

# Define the file paths
input_file_path = r'C:\ChatGPT\peak.txt'  # Update with the correct file path
output_file_path = r'C:\ChatGPT\Scramble.txt'  # Update with the desired output file path

try:
    # Read the input file
    with open(input_file_path, 'r') as input_file:
        peak_text = input_file.read()
except FileNotFoundError:
    print(f"File not found at {input_file_path}. Make sure the file exists.")
    exit(1)

# Convert the text to a list of characters for shuffling
peak_chars = list(peak_text)
random.shuffle(peak_chars)

# Join the shuffled characters back into a string
scrambled_text = ''.join(peak_chars)

# Write the scrambled text to the output file
try:
    with open(output_file_path, 'w') as output_file:
        output_file.write(scrambled_text)
    print(f"Scrambled text saved to {output_file_path}.")
except Exception as e:
    print(f"An error occurred while writing to {output_file_path}: {str(e)}")
