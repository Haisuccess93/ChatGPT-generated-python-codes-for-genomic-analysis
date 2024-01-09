# Define the file paths
input_file_path_1 = input("Enter the path to the first file: ")
input_file_path_2 = input("Enter the path to the second file: ")
output_file_path = r'C:\ChatGPT\counts.txt'  # Output file path

try:
    # Read the sequences from the first file
    with open(input_file_path_1, 'r') as file1:
        sequences = file1.read().strip().upper()  # Convert to uppercase

    # Read the content of the second file
    with open(input_file_path_2, 'r') as file2:
        content2 = file2.read().strip().upper()  # Convert to uppercase

except FileNotFoundError:
    print("File not found. Make sure the files exist.")
    exit(1)

# Define the length of the nucleotide sequence (10 nucleotides)
sequence_length = 10

# Initialize a dictionary to store counts of unique sequences
sequence_counts = {}

# Iterate through the sequences in the first file
for i in range(len(sequences) - sequence_length + 1):
    sequence = sequences[i:i + sequence_length]
    if sequence not in sequence_counts:
        # Count the occurrences of the sequence in the second file
        count = content2.count(sequence)
        sequence_counts[sequence] = count

# Write the results to the output file
try:
    with open(output_file_path, 'w') as output_file:
        for sequence, count in sequence_counts.items():
            output_file.write(f"{sequence}\t{count}\n")

    print(f"Results saved to {output_file_path}.")
except Exception as e:
    print(f"An error occurred while writing to {output_file_path}: {str(e)}")
