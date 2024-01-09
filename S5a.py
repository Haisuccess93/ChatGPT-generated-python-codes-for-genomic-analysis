# Define file paths for Mac
input_file_path = '/Users/isabellaswan/python/input.txt'
output_file_path = '/Users/isabellaswan/python/pieces.txt'

# Read the content from input file
with open(input_file_path, 'r') as file:
    nucleotides = file.read().strip()

# Break into 100-letter sections
sections = [nucleotides[i:i+100] for i in range(0, len(nucleotides), 100)]

# Write sections to the output file
with open(output_file_path, 'w') as file:
    for i, section in enumerate(sections):
        start_idx = i * 100 + 1
        end_idx = min((i+1) * 100, len(nucleotides))
        header = f'>{start_idx}-{end_idx}\n'
        file.write(header + section + '\n')

print(f"Sections written to {output_file_path}")

