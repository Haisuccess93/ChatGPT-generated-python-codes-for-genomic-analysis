import pandas as pd

# Prompt for input file names
first_file_name = input("Enter the name of the first file: ")
second_file_name = input("Enter the name of the second file: ")

# Prompt for output file names
first_output_name = input("Enter the name for the first output CSV file (without extension): ")
second_output_name = input("Enter the name for the second output CSV file (without extension): ")

# Read the first file and print the DataFrame
try:
    first_df = pd.read_csv(first_file_name, header=None)
    print("First DataFrame:")
    print(first_df.head())
except Exception as e:
    print(f"An error occurred while reading the first file: {e}")
    exit()

# Read the second file and print the DataFrame
try:
    second_df = pd.read_csv(second_file_name, header=None)
    print("Second DataFrame:")
    print(second_df.head())
except Exception as e:
    print(f"An error occurred while reading the second file: {e}")
    exit()

# Write the first DataFrame to a CSV file
first_output_csv_name = f"{first_output_name}.csv"
try:
    first_df.to_csv(first_output_csv_name, header=False, index=False)
    print(f"CSV file {first_output_csv_name} has been created.")
except Exception as e:
    print(f"An error occurred while writing the first output file: {e}")

# Write the second DataFrame to a CSV file
second_output_csv_name = f"{second_output_name}.csv"
try:
    second_df.to_csv(second_output_csv_name, header=False, index=False)
    print(f"CSV file {second_output_csv_name} has been created.")
except Exception as e:
    print(f"An error occurred while writing the second output file: {e}")
