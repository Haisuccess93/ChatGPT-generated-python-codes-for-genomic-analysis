import os
import time

# Function to search for names in FASTA file and extract sequences
def search_and_extract(fasta_file, names_file, output_file):
    names_set = set()
    with open(names_file, 'r') as names_input:
        for line in names_input:
            name = line.strip().split(' ')[0]  # Extract the name without additional information
            names_set.add(name)

    sequences = {}
    current_name = None

    with open(fasta_file, 'r') as fasta_input:
        for line in fasta_input:
            line = line.strip()
            if line.startswith('>'):
                current_name = line[1:].split(' ')[0]  # Extract the name without additional information
                if current_name in names_set:
                    sequences[current_name] = ""
            elif current_name and current_name in names_set:
                sequences[current_name] += line

    # Write the sequences to the output file
    with open(output_file, 'w') as fasta_output:
        for name, sequence in sequences.items():
            fasta_output.write(f'>{name}\n{sequence}\n')

# Prompt the user for file paths
names_file_path = input("Enter the path to the names file: ")
fasta_file_path = input("Enter the path to the FASTA file: ")

# Record the start time
start_time = time.time()

# Calculate the number of unique names
names_set = set()
with open(names_file_path, 'r') as names_input:
    for line in names_input:
        name = line.strip().split(' ')[0]  # Extract the name without additional information
        names_set.add(name)

output_file_path = os.path.join(os.path.dirname(fasta_file_path), 'O-Plus.fasta')

if os.path.isfile(fasta_file_path) and os.path.isfile(names_file_path):
    search_and_extract(fasta_file_path, names_file_path, output_file_path)
    print(f'Extraction completed. Results saved in {output_file_path}')
else:
    print('One or more of the specified files does not exist.')

# Calculate and display the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")
