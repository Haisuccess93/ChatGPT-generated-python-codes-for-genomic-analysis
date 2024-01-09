import random

# Define file paths for Mac
input_file_path = '/Users/isabellaswan/python/peak.txt'
output_file_path = '/Users/isabellaswan/python/scrambled.txt'

# Read the content from input file
with open(input_file_path, 'r') as file:
    content = file.read()

# Randomly shuffle the characters
shuffled_content = list(content)
random.shuffle(shuffled_content)
shuffled_content = ''.join(shuffled_content)

# Write the shuffled content to the output file
with open(output_file_path, 'w') as file:
    file.write(shuffled_content)

print(f"Content shuffled and saved to {output_file_path}")

