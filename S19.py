def extract_values(input_file):
    unique_values = set()
    with open(input_file, 'r') as file:
        for line in file:
            value = line.split('\t')[0]
            if value not in unique_values:
                unique_values.add(value)
    return unique_values

def create_output_file(unique_values, output_folder):
    output_file_path = f"{output_folder}/output_{len(unique_values)}.txt"
    with open(output_file_path, 'w') as file:
        for value in unique_values:
            file.write(f"{value}\n")
    return output_file_path

def main():
    input_file = input("Please provide the path to the input file: ")
    output_folder = '/Users/isabellaswan/python'

    unique_values = extract_values(input_file)
    output_file_path = create_output_file(unique_values, output_folder)

    print(f"Output file created at: {output_file_path}")

if __name__ == "__main__":
    main()

