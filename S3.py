def filter_nucleotides(input_file, output_file):
    # Define nucleotide symbols
    nucleotides = set('acgt')

    try:
        with open(input_file, 'r') as file:
            content = file.read()

            # Filter nucleotides, keeping only lowercase nucleotide characters
            filtered_content = ''.join(char for char in content if char.lower() in nucleotides)

        # Write filtered content to the output file
        with open(output_file, 'w') as output:
            output.write(filtered_content)
        
        print("Filtered nucleotides saved to", output_file)

    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")


# Get input and output file names from user
input_file_name = input("Enter input file name: ")
output_file_name = input("Enter output file name: ")

# Call function to filter nucleotides
filter_nucleotides(input_file_name, output_file_name)
