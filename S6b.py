def count_10nt_sequences(input_file_path, reference_file_path):
    sequence_counts = {}
    
    try:
        # Read the content of the reference file
        with open(reference_file_path, 'r') as reference_file:
            reference_text = reference_file.read()
        
        # Read and process the input file
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if len(line) >= 10:
                    for i in range(len(line) - 9):
                        sequence = line[i:i+10]
                        count = reference_text.count(sequence)
                        sequence_counts[sequence] = sequence_counts.get(sequence, 0) + count
    except FileNotFoundError:
        print("One or both input files not found.")
        return None
    
    return sequence_counts

def write_counts_to_file(output_file_path, sequence_counts):
    try:
        with open(output_file_path, 'w') as output_file:
            for sequence, count in sequence_counts.items():
                output_file.write(f"{sequence}\t{count}\n")
        print(f"Results saved to '{output_file_path}'")
    except Exception as e:
        print(f"An error occurred while writing to the output file: {str(e)}")

# Get user input for input and output file paths
input_file_path = input("Enter the path to the first input file: ")
reference_file_path = input("Enter the path to the second reference file: ")
output_file_path = r'C:\chatgptclass\counts.txt'  # Output file path

# Count unique 10nt sequences
sequence_counts = count_10nt_sequences(input_file_path, reference_file_path)

if sequence_counts:
    # Write results to the output file
    write_counts_to_file(output_file_path, sequence_counts)
