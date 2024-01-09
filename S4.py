import random

def shuffle_nucleotides(sequence):
    # Convert the sequence to a list to allow shuffling
    sequence_list = list(sequence)
    
    # Shuffle the nucleotides in the list
    random.shuffle(sequence_list)
    
    # Join the shuffled list back into a string
    shuffled_sequence = ''.join(sequence_list)
    
    return shuffled_sequence

# Prompting user for input file name
input_file = input("Enter the name of the input text file containing the nucleotide sequence: ")

try:
    # Read the sequence from input file
    with open(input_file, 'r') as file:
        sequence = file.read().strip()

    # Shuffle the positions of nucleotides in the sequence
    shuffled_sequence = shuffle_nucleotides(sequence)

    # Prompting user for output file name
    output_file = input("Enter the name of the output file for the shuffled nucleotides: ")

    # Write the shuffled nucleotide sequence to an output file
    with open(output_file, 'w') as file:
        file.write(shuffled_sequence)

    print(f"Shuffled nucleotide sequence has been saved to {output_file}")

except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
except Exception as e:
    print(f"An error occurred: {e}")
