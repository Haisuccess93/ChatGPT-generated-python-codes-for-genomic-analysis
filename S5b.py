# Define the file paths
input_file_path = r'C:\ChatGPT\peak.txt'  # Update with the correct file path
output_file_path = r'C:\ChatGPT\pieces.txt'  # Update with the desired output file path

try:
    # Read the input file
    with open(input_file_path, 'r') as input_file:
        nucleotide_sequence = input_file.read().strip()
except FileNotFoundError:
    print(f"File not found at {input_file_path}. Make sure the file exists.")
    exit(1)

# Define the length of each section
section_length = 100

# Split the sequence into sections and format in FASTA format
sections = [nucleotide_sequence[i:i + section_length] for i in range(0, len(nucleotide_sequence), section_length)]

# Write the sections to the output file in FASTA format
try:
    with open(output_file_path, 'w') as output_file:
        for i, section in enumerate(sections, start=1):
            output_file.write(f">Sequence_{i}\n")
            output_file.write(section + "\n")
    print(f"Sequence sections saved to {output_file_path}.")
except Exception as e:
    print(f"An error occurred while writing to {output_file_path}: {str(e)}")
