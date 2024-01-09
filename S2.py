def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_seq = sequence[::-1]  # Reverse the sequence
    reverse_complement_seq = ''.join(complement[base] for base in reverse_seq)
    return reverse_complement_seq

# Prompting user for input file name
input_file = input("Enter the name of the input text file containing the nucleotide sequence: ")

try:
    # Read the sequence from input file
    with open(input_file, 'r') as file:
        sequence = file.read().strip()

    # Get the reverse complement of the sequence
    reverse_comp_sequence = reverse_complement(sequence)

    # Write the reverse complement sequence to an output file
    output_file = "reverse_complemented.txt"
    with open(output_file, 'w') as file:
        file.write(reverse_comp_sequence)

    print(f"Reverse complemented sequence has been saved to {output_file}")

except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
except Exception as e:
    print(f"An error occurred: {e}")
