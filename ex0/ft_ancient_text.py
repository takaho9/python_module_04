import sys


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery ===")
    path = sys.argv[1]
    try:
        print(f"Accessing file '{path}'")
        f = open(path, "r")
    except OSError as e:
        print(f"Error opening file '{path}': {e}")
        return

    print("---\n")
    print(f.read())
    print("---")
    f.close()
    print(f"File '{path}' closed.")


if __name__ == "__main__":
    main()
