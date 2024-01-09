import os

# Function to read the first 100 sequences from a FASTA file and save to a text file
def extract_first_100_sequences(fasta_file):
    sequences = {}
    current_name = None
    counter = 0

    with open(fasta_file, 'r') as fasta_input:
        for line in fasta_input:
            line = line.strip()
            if line.startswith('>'):
                current_name = line[1:]
                sequences[current_name] = ""
                counter += 1
            elif current_name:
                sequences[current_name] += line
            if counter >= 100:
                break

    return sequences

# Prompt the user for the FASTA file path
fasta_file_path = input("Enter the path to the FASTA file: ")

if os.path.isfile(fasta_file_path):
    output_file_path = os.path.splitext(fasta_file_path)[0] + '.txt'
    sequences = extract_first_100_sequences(fasta_file_path)

    with open(output_file_path, 'w') as output_file:
        for name, sequence in sequences.items():
            output_file.write(f'>{name}\n{sequence}\n')

    print(f'First 100 sequences saved to {output_file_path}')
else:
    print('The specified FASTA file does not exist.')
