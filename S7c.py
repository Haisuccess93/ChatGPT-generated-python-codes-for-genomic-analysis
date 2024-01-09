import os

def extract_20_nucleotide_sequences(file_path):
    # Read the file and extract 20-nucleotide sequences starting from the first nucleotide
    with open(file_path, 'r') as file:
        contents = file.read().replace('\n', '')  # Remove newline characters
        sequences = [contents[i:i+20] for i in range(0, len(contents) - 19)]
    return sequences

def count_occurrences(sequences, file_path):
    # Read the second file and count occurrences of each 20-nucleotide sequence
    with open(file_path, 'r') as file:
        content = file.read().replace('\n', '')  # Remove newline characters
        sequence_counts = {sequence: content.count(sequence) for sequence in sequences}
    return sequence_counts

def save_counts_to_file(sequence_counts, output_file):
    # Save the sequence counts to the output file
    with open(output_file, 'w') as output:
        for sequence, count in sequence_counts.items():
            output.write(f"{sequence}\t{count}\n")

# Specify input files and output directory
file1 = input("Enter the path to the first file containing 20-nucleotide sequences: ")
file2 = input("Enter the path to the second file: ")
output_file = r"C:\CHATGPTclass\countsDA12.txt"

# Extract 20-nucleotide sequences from the first file
sequences = extract_20_nucleotide_sequences(file1)

# Count the occurrences of each 20-nucleotide sequence in the second file
sequence_counts = count_occurrences(sequences, file2)

# Save the sequence counts to the output file
save_counts_to_file(sequence_counts, output_file)

print("Counting completed. Results saved in 'countsDA12.txt' in the specified folder.")
