import pandas as pd

# Function to convert Excel files to CSV
def excel_to_csv(file_path, output_file):
    df = pd.read_excel(file_path)
    df.to_csv(output_file, sep='\t', index=False)

# Function to find matching strings between columns A and B
def find_matches(file_a, file_b):
    df_a = pd.read_csv(file_a, sep='\t')
    df_b = pd.read_csv(file_b, sep='\t')

    matches = []
    for index_a, row_a in df_a.iterrows():
        string_a = row_a.iloc[0]  # Assuming the first column contains strings
        for index_b, row_b in df_b.iterrows():
            string_b = row_b.iloc[0]
            if string_a == string_b:
                matches.append(string_a)

    return matches

# Function to process matches and generate output
def process_matches(matches, file_a, file_b, output_file):
    df_a = pd.read_csv(file_a, sep='\t')
    df_b = pd.read_csv(file_b, sep='\t')

    results = []
    for match in matches:
        # Check for match in A
        match_rows_a = df_a[df_a.iloc[:, 0] == match]
        for index_a, row_a in match_rows_a.iterrows():
            # Check for match in B
            match_rows_b = df_b[df_b.iloc[:, 0] == match]
            for index_b, row_b in match_rows_b.iterrows():
                # Extract characters following the second and third tab
                result_row = [match, row_a.iloc[1], row_a.iloc[2], row_b.iloc[1], row_b.iloc[2]]
                results.append(result_row)

    # Create DataFrame from results
    result_df = pd.DataFrame(results, columns=['Matched Characters', 'A_col2', 'A_col3', 'B_col2', 'B_col3'])

    # Save results to Excel file
    result_df.to_excel(output_file, index=False)

# Prompt for input Excel files
file_path_a = input("Enter path for Excel file A: ")
file_path_b = input("Enter path for Excel file B: ")

# Convert Excel files to CSV
excel_to_csv(file_path_a, 'A.csv')
excel_to_csv(file_path_b, 'B.csv')

# Find matches between A and B
matches = find_matches('A.csv', 'B.csv')

# Process matches and generate output
process_matches(matches, 'A.csv', 'B.csv', 'output.xlsx')
