import sys


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    path = sys.argv[1]
    try:
        print(f"Accessing file '{path}'")
        f = open(path, "r")
    except OSError as e:
        print(f"Error opening file '{path}': {e}")
        return

    content = f.read()
    print("---")
    print()
    print(content, end="")
    print()
    print("---")
    f.close()
    print(f"File '{path}' closed.")
    print()
    print("Transform data:")
    print("---")
    print()
    content = content.replace("\n", "#\n")
    print(content, end="")
    print()
    print("---")
    new_file_path = input("Enter new file name (or empty): ")
    if new_file_path == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file_path}'")
    try:
        f = open(new_file_path, "w")
    except OSError as e:
        print(f"Error opening file '{new_file_path}': {e}")
        print("Data not saved.")
        return
    f.write(content)
    print(f"Data saved in file '{new_file_path}'.")
    f.close()


if __name__ == "__main__":
    main()
