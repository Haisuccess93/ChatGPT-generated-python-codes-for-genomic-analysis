def read_sequences(file_path):
    sequences = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) >= 20:
                for i in range(len(line) - 19):
                    sequences.add(line[i:i + 20])
    return sequences

def count_sequences(input_file, target_file, output_file):
    input_sequences = read_sequences(input_file)
    target_text = ""
    
    with open(target_file, 'r') as file:
        target_text = file.read()

    results = {}
    for sequence in input_sequences:
        count = target_text.count(sequence)
        results[sequence] = count

    with open(output_file, 'w') as outfile:
        for sequence, count in results.items():
            outfile.write(f"{sequence}\t{count}\n")

if __name__ == '__main__':
    input_file = input("Enter the path to the first specified .txt file: ")
    target_file = input("Enter the path to the second specified .txt file: ")
    output_file = r'C:\ChatGPT\DA12Uprinsloo.txt'  # Output file location

    count_sequences(input_file, target_file, output_file)
    print(f"Results written to {output_file}")
