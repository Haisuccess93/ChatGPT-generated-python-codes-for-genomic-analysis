def divide_sequence(sequence):
    sequences = []
    start = 0
    end = 100
    
    while start < len(sequence):
        sequences.append(sequence[start:end])
        start = end
        end += 100
    
    return sequences

# Prompting user for input file name
input_file_path = input("Enter the path of the input text file containing the nucleotide sequence: ")

try:
    # Read the sequence from input file
    with open(input_file_path, 'r') as file:
        sequence = file.read().strip()

    # Divide the sequence into portions of 100 nucleotides
    divided_sequences = divide_sequence(sequence)

    # Prompting user for output file name
    output_file_name = input("Enter the name of the output file for the divided sequences: ")

    # Write each 100-nucleotide sequence to an output file
    with open(output_file_name, 'w') as file:
        for i, seq in enumerate(divided_sequences):
            start_pos = i * 100 + 1
            end_pos = min((i + 1) * 100, len(sequence))
            file.write(f">{start_pos}-{end_pos}\n{seq}\n")

    print(f"Sequences divided into portions of 100 nucleotides each have been saved to {output_file_name}")

except FileNotFoundError:
    print("File not found. Please enter a valid file path.")
except Exception as e:
    print(f"An error occurred: {e}")
