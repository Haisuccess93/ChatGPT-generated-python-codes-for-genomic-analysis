import random

# Function to scramble the characters of a string
def scramble_text(text):
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)

# Input file path
input_path = input("Enter the input file name (e.g., input.txt): ")
input_file = f"C:\\CHATGPTclass\\{input_path}"

# Output file path
output_path = input("Enter the output file name (e.g., output.txt): ")
output_file = f"C:\\CHATGPTclass\\{output_path}"

try:
    # Read the contents of the input file
    with open(input_file, 'r') as file:
        text = file.read()

    # Scramble the text
    scrambled_text = scramble_text(text)

    # Write the scrambled text to the output file
    with open(output_file, 'w') as file:
        file.write(scrambled_text)

    print(f"Text has been scrambled and saved to {output_path}")
except FileNotFoundError:
    print(f"File not found: {input_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
