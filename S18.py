import os

def read_names_from_file(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file)

def filter_fasta(input_fasta, output_fasta, names_to_remove):
    with open(input_fasta, 'r') as input_file, open(output_fasta, 'w') as output_file:
        current_name = None
        skip_entry = False
        for line in input_file:
            if line.startswith('>'):
                current_name = line[1:].strip()
                skip_entry = current_name in names_to_remove
            if not skip_entry:
                output_file.write(line)

if __name__ == "__main__":
    names_file = input("Enter the path to the file containing names to remove: ")
    input_fasta_file = input("Enter the path to the input FASTA file: ")
    output_fasta_name = input("Enter the name for the output FASTA file: ")

    output_fasta_file = os.path.join("C:\\ChatGPT", output_fasta_name)

    names_to_remove = read_names_from_file(names_file)

    filter_fasta(input_fasta_file, output_fasta_file, names_to_remove)

    print(f"Filtered FASTA file saved to {output_fasta_file}")
