def count_fasta_sequences(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        count = sum(1 for line in lines if line.startswith('>'))
        print(f"The file '{file_path}' contains {count} sequences.")

file_path = input("Enter the file path of the FASTA file: ")
count_fasta_sequences(file_path)

