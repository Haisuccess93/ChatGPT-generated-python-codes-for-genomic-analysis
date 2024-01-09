def count_greater_than_signs(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            count = content.count('>')
            return count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    file_path = input("Enter the path of the file: ")
    count = count_greater_than_signs(file_path)

    if count is not None:
        print(f"Number of '>' signs in the file: {count}")

if __name__ == "__main__":
    main()
