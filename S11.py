import pandas as pd

# Prompt for input and output file names
input_file_name = input("Enter the name of the input text file: ")
output_file_name = input("Enter the name for the output Excel file (without extension): ")

# Combine the current working directory with the provided file name
output_excel_path = f"{output_file_name}.xlsx"

# Read the text file
try:
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
except Exception as e:
    print(f"An error occurred while reading the input file: {e}")
    exit()

# Create a DataFrame from the lines of the text file
data = [line.strip().split('\t') for line in lines]

# Convert the data to an Excel file
try:
    df = pd.DataFrame(data)
    df.to_excel(output_excel_path, header=False, index=False)
    print(f"Text file '{input_file_name}' has been converted to Excel file '{output_excel_path}'.")
except Exception as e:
    print(f"An error occurred while writing the output Excel file: {e}")
