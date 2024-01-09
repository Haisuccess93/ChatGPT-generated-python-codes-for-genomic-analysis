import os
import re

def count_fasta_reads(file_path):
    try:
        # Open the specified file in read mode
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Count the number of FASTA reads
            fasta_reads = re.findall(r'^>.*?$', content, flags=re.MULTILINE)
            count = len(fasta_reads)
            
            # Create the output file name
            output_file_name = f"{os.path.basename(file_path)}_{count}.txt"

            # Create the output file path
            output_file_path = os.path.join("C:\\CHATGPTclass", output_file_name)

            # Write the count to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(str(count))

            print(f"Counted {count} FASTA reads in the file.")
            print(f"Output file '{output_file_name}' created in 'C:\\CHATGPTclass' folder.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")

# Get the input file path from the user
user_file_path = input("Enter the path of the file: ")

# Call the function to count and create the output file
count_fasta_reads(user_file_path)
