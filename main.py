from stats import book_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_report(sys.argv[1])

if __name__ == "__main__":
    main()
