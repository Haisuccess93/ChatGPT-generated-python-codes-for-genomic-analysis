# Define the input and output file paths
input_file_path = "/Users/meredithshaddix/Documents/CHATGPT/dirty.txt"
output_file_path = "/Users/meredithshaddix/Documents/CHATGPT/clean.txt"

# Function to clean a string by removing unwanted characters
def clean_string(input_str):
    # Filter for characters A, G, C, and T (case-insensitive)
    clean_chars = [char for char in input_str if char.upper() in ["A", "G", "C", "T"]]
    return "".join(clean_chars)

# Read the input string from the input file
try:
    with open(input_file_path, "r") as input_file:
        input_string = input_file.read()
except FileNotFoundError:
    print(f"Input file '{input_file_path}' not found.")
    exit(1)

# Clean the input string
cleaned_string = clean_string(input_string)

# Write the cleaned string to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(cleaned_string)

print(f"Cleaned string saved to '{output_file_path}'.")
