def generate_fasta(seq, line_length=100):
    # Split the sequence into lines of specified length
    lines = [seq[i:i+line_length] for i in range(0, len(seq), line_length)]
    
    # Create the Fasta format with position information
    fasta_lines = []
    for i, line in enumerate(lines):
        start_position = i * line_length + 1
        end_position = min((i + 1) * line_length, len(seq))
        header = f">Position {start_position}-{end_position}\n{line}"
        fasta_lines.append(header)
    
    # Add the position information for the last piece
    last_piece_start = (len(lines) - 1) * line_length + 1
    last_piece_end = len(seq)
    last_piece_header = f">Position {last_piece_start}-{last_piece_end}\n{lines[-1]}"
    fasta_lines[-1] = last_piece_header
    
    fasta_str = "\n".join(fasta_lines)
    
    return fasta_str


def main():
    # Read input from the file
    input_file_path = r"C:\CHATGPTclass\input.txt"
    with open(input_file_path, "r") as input_file:
        linear_string = input_file.read().strip()

    # Generate Fasta format with 100 characters per line
    fasta_str = generate_fasta(linear_string, line_length=100)

    # Write the Fasta format to a new file
    output_file_path = r"C:\CHATGPTclass\pieces.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write(fasta_str)

    print("Fasta formatted pieces with positions saved to:", output_file_path)


if __name__ == "__main__":
    main()




