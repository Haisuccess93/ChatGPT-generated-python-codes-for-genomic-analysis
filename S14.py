import pandas as pd

def remove_quotation_marks(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    cleaned_lines = [line.replace('"', '') for line in lines]

    with open(file_name, 'w') as file:
        file.writelines(cleaned_lines)

    print(f"Quotation marks removed from {file_name}.")

def csv_to_txt():
    input_file = input("Enter the input CSV file name: ")
    output_file = input("Enter the output txt file name: ")

    try:
        # Read the CSV file
        df = pd.read_csv(input_file)

        # Write the data to a tab-separated text file
        df.to_csv(output_file, sep='\t', index=False)

        print(f"Conversion complete. Results saved in {output_file}.")

        # Remove quotation marks from the output file
        remove_quotation_marks(output_file)

    except OSError as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    csv_to_txt()
