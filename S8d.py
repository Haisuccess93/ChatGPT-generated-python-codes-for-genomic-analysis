def count_occurrences(file_path, search_text):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content.count(search_text)
    except FileNotFoundError:
        print("File not found.")
        return 0

if __name__ == "__main__":
    file_path = input("Enter the path of the file: ")
    search_text = ">"
    occurrences = count_occurrences(file_path, search_text)
    print(f"The text '{search_text}' occurs {occurrences} time(s) in the file.")