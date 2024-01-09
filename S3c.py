def clean_sequence(input_sequence):
    allowed_characters = set("atgcATGC")
    cleaned_sequence = ''.join(char for char in input_sequence if char in allowed_characters)
    return cleaned_sequence

def process_input_file(input_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read().strip()

    cleaned_content = clean_sequence(content)
    return cleaned_content

def write_to_output_file(output_file_path, content):
    with open(output_file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    input_file_path = r"C:\CHATGPTclass\dirty.txt"
    output_file_path = r"C:\CHATGPTclass\clean.txt"

    cleaned_content = process_input_file(input_file_path)
    write_to_output_file(output_file_path, cleaned_content)

    print("Processing completed. Result written to clean.txt")
