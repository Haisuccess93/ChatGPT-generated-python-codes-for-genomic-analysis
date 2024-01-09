from collections import Counter

def find_similar_sequences(seq1, seq2, min_length):
    similar_sequences = set()

    for length in range(min_length, min(len(seq1), len(seq2)) + 1):
        seq1_set = set(seq1[i:i + length] for i in range(len(seq1) - length + 1))
        seq2_set = set(seq2[i:i + length] for i in range(len(seq2) - length + 1))

        similar_sequences.update(seq1_set.intersection(seq2_set))

    return similar_sequences

# Prompting user for input file paths
input_file_path_1 = input("Enter the path of the first input text file containing nucleotide sequence: ")
input_file_path_2 = input("Enter the path of the second input text file containing nucleotide sequence: ")

try:
    # Read sequences from input files
    with open(input_file_path_1, 'r') as file1, open(input_file_path_2, 'r') as file2:
        sequence_1 = file1.read().strip()
        sequence_2 = file2.read().strip()

    # Minimum length of identical sequence
    min_length = 10

    # Find identical sequences at least 10 nucleotides long
    identical_sequences = find_similar_sequences(sequence_1, sequence_2, min_length)

    # Count occurrences of identical sequences
    sequence_counts = Counter(identical_sequences)

    # Generate output content with unique identical sequences sorted by length
    output_content = []
    for seq, count in sequence_counts.items():
        seq_length = len(seq)
        header = f">{seq_length}-mer"
        if count > 1:
            header += f"_{count}_occurrences"
        output_content.append((header, seq))

    # Sort sequences by length in ascending order
    sorted_sequences = sorted(output_content, key=lambda x: len(x[1]))

    # Prompting user for output file name
    output_file_name = input("Enter the name of the output file to save unique identical sequences in FASTA-like format: ")

    # Write unique identical sequences to an output file in FASTA-like format
    with open(output_file_name, 'w') as output_file:
        for header, seq in sorted_sequences:
            output_file.write(f"{header}\n{seq}\n")

    print(f"Unique identical sequences greater than {min_length} nucleotides long have been saved to {output_file_name} in ascending order of length")

except FileNotFoundError:
    print("File not found. Please enter valid file paths.")
except Exception as e:
    print(f"An error occurred: {e}")
