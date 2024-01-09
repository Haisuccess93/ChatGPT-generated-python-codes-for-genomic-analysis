def count_sequences(input_file, target_file, output_folder):
    with open(input_file, 'r') as f:
        sequence = f.read()

    with open(target_file, 'r') as f:
        target_sequence = f.read()

    output_file = f"{output_folder}/DA12counts.txt"
    with open(output_file, 'w') as f:
        for i in range(len(sequence) - 19):
            seq = sequence[i:i+20]
            count = target_sequence.count(seq)
            f.write(f"{seq}\t{count}\n")

    print(f"Results saved in {output_folder}/DA12counts.txt")

input_file = input("Enter the path of the input file: ")
target_file = input("Enter the path of the target file: ")
output_folder = "/Users/isabellaswan/python"

count_sequences(input_file, target_file, output_folder)

