import os
import pandas as pd

# Convert Excel file to CSV with rows separated by tabs
def excel_to_csv(input_excel, output_csv):
    df = pd.read_excel(input_excel)
    df.to_csv(output_csv, sep='\t', index=False)

# Extract first column content before the first tab
def extract_read_names(input_csv, output_read_names):
    with open(input_csv, 'r') as file:
        with open(output_read_names, 'w') as output:
            for line in file:
                read_name = line.split('\t')[0]
                output.write(f">{read_name}\n")

# Find sequences corresponding to read names in FASTA file
def find_sequences(input_fasta, read_names_file, output_fasta, output_read_names):
    read_names = set()
    with open(read_names_file, 'r') as file:
        for line in file:
            if line.startswith('>'):
                read_names.add(line.strip()[1:])

    sequences = {}
    current_read_name = ''
    with open(input_fasta, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_read_name = line[1:]
                if current_read_name in read_names:
                    sequences[current_read_name] = []
            elif current_read_name in sequences:
                sequences[current_read_name].append(line)

    with open(output_fasta, 'w') as output:
        for read_name, sequence in sequences.items():
            output.write(f">{read_name}\n")
            for i, seq in enumerate(sequence):
                output.write(f"{seq}\n")

    with open(output_read_names, 'w') as output:
        for read_name in read_names:
            output.write(f">{read_name}\n")

    print(f"Sequences corresponding to read names have been saved to {output_fasta}")
    print(f"Read names have been saved to {output_read_names}")

if __name__ == "__main__":
    # Prompting for input file paths and output file names
    excel_file = input("Enter the path of the Excel file: ")
    output_csv_file = "output.csv"
    output_read_names_file = "read_names.fasta"
    fasta_file = input("Enter the path of the FASTA file: ")
    output_fasta_file = input("Enter the name for the output FASTA file: ")

    # Convert Excel file to CSV with rows separated by tabs
    excel_to_csv(excel_file, output_csv_file)

    # Extract first column content before the first tab
    extract_read_names(output_csv_file, output_read_names_file)

    # Find sequences corresponding to read names in FASTA file
    find_sequences(fasta_file, output_read_names_file, output_fasta_file, output_read_names_file)
