def reverse_complement(character):
    if character == 'A':
        return 'T'
    elif character == 'T':
        return 'A'
    elif character == 'G':
        return 'C'
    elif character == 'C':
        return 'G'
    else:
        return character

def process_input_file(input_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read().strip()

    reversed_complemented_content = ''.join([reverse_complement(char) for char in content[::-1]])

    return reversed_complemented_content

def write_to_output_file(output_file_path, content):
    with open(output_file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    input_file_path = r"C:\CHATGPTclass\input.txt"
    output_file_path = r"C:\CHATGPTclass\reversecomplemented 2.txt"

    processed_content = process_input_file(input_file_path)
    write_to_output_file(output_file_path, processed_content)

    print("Processing completed. Result written to reversecomplemented 2.txt")
