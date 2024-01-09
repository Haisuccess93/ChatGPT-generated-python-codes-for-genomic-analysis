# Define the input and output file paths
input_file_path = '/Users/isabellaswan/python/dirty.txt'
output_file_path = '/Users/isabellaswan/python/clean.txt'

# Read the input file and filter out unwanted characters
with open(input_file_path, 'r') as input_file:
    dirty_string = input_file.read()
    clean_string = ''.join(char for char in dirty_string if char.upper() 
in 'AGCT')

# Write the clean string to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(clean_string)

print(f"Cleaned data written to {output_file_path}")

