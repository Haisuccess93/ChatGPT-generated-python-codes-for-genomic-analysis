def split_nucleotides_to_fasta(input_sequence, chunk_size=100):
    num_chunks = len(input_sequence) // chunk_size
    remainder = len(input_sequence) % chunk_size
    if remainder > 0:
        num_chunks += 1

    fasta_text = ""
    for i in range(num_chunks):
        start = i * chunk_size
        end = start + chunk_size
        chunk = input_sequence[start:end]
        fasta_text += f">chunk_{i + 1}\n{chunk}\n"

    return fasta_text

# Input file path
input_path = input("Enter the input file name (e.g., input.txt): ")

# Output file path for both text and FASTA
output_path = input("Enter the output file name (e.g., output.txt): ")

try:
    # Read the contents of the input file
    with open(input_path, 'r') as file:
        nucleotide_sequence = file.read()

    # Split the nucleotide sequence and create the FASTA content
    fasta_content = split_nucleotides_to_fasta(nucleotide_sequence)

    # Write the FASTA content and save it in the same output document as .txt
    with open(output_path, 'w') as output_file:
        output_file.write(fasta_content)

    print(f"FASTA chunks have been saved to {output_path}")
except FileNotFoundError:
    print(f"File not found: {input_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
