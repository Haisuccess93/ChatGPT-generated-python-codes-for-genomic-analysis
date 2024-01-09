import docx2txt
import os

def convert_to_plain_text(input_file):
    # Check if the file is a .docx file
    if not input_file.endswith('.docx'):
        print("Please provide a .docx file.")
        return

    # Convert the Word document to plain text
    text = docx2txt.process(input_file)

    # Create a name for the output file
    output_file = os.path.splitext(input_file)[0] + '.txt'

    # Write the plain text to a new file
    with open(output_file, 'w', encoding="utf-8") as text_file:
        text_file.write(text)

    print(f"Conversion complete. Plain text file saved as: {output_file}")

if __name__ == "__main__":
    input_file = input("Enter the path to the Word file: ")
    convert_to_plain_text(input_file)
