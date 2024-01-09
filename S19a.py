# Function to extract unique read names from a BLAST output file
def extract_unique_reads(input_file, output_file):
    unique_reads = set()

    with open(input_file, 'r') as blast_file:
        for line in blast_file:
            # Assuming that the read name is in the first column of the BLAST output
            columns = line.strip().split('\t')
            if columns:
                read_name = columns[0]
                unique_reads.add(read_name)

    with open(output_file, 'w') as output:
        for read_name in unique_reads:
            output.write(read_name + '\n')

if __name__ == '__main__':
    blast_input_file = input("Enter the BLAST output file path: ")
    unique_reads_output_file = "unique_blast.txt"

    extract_unique_reads(blast_input_file, unique_reads_output_file)

    print(f"Unique read names extracted and saved to '{unique_reads_output_file}'.")
