# Define the input and output file paths
input_file_path = "/Users/meredithshaddix/Documents/CHATGPT/input.txt"
output_file_path = "/Users/meredithshaddix/Documents/CHATGPT/reversecomplemented.txt"

# Function to reverse and complement a string
def reverse_complement(input_str):
    complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(complement_dict.get(char, char) for char in input_str[::-1])

# Read the input string from the input file
try:
    with open(input_file_path, "r") as input_file:
        input_string = input_file.read()
except FileNotFoundError:
    print(f"Input file '{input_file_path}' not found.")
    exit(1)

# Reverse complement the input string
result_string = reverse_complement(input_string)

# Write the result to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(result_string)

print(f"Reverse complemented string saved to '{output_file_path}'.")
