import random

# Define the file paths
input_file_path = "/Users/meredithshaddix/Documents/CHATGPT/peak.txt"
output_file_path = "/Users/meredithshaddix/Documents/CHATGPT/scrambled.txt"

# Read the input string from the input file
with open(input_file_path, 'r') as input_file:
    input_string = input_file.read()

# Convert the input string to a list of characters and shuffle it
input_characters = list(input_string)
random.shuffle(input_characters)

# Join the shuffled characters back into a string
shuffled_string = ''.join(input_characters)

# Write the shuffled string to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(shuffled_string)

print("Scrambled string has been written to", output_file_path)
