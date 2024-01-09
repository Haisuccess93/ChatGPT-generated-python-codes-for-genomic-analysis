def extract_values(file_path):
    values = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 1:
                key = parts[0]
                value = parts[3] if len(parts) > 3 else ""
                values[key] = value
    return values

def find_and_write_matches(file1, file2, output_file):
    data_file1 = extract_values(file1)
    data_file2 = extract_values(file2)

    with open(output_file, 'w') as output:
        for key in data_file1:
            if key in data_file2:
                line = f"{key}\t{data_file1[key]}\t{data_file2[key]}\n"
                output.write(line)

# Input file paths from the user
file1_path = input("Enter the path of the first file: ")
file2_path = input("Enter the path of the second file: ")

# Output file path
output_path = r"C:\CHATGPTclass\same_hits.txt"

# Call the function to find matches and write the output file
find_and_write_matches(file1_path, file2_path, output_path)
