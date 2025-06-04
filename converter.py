import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Konwerter plików')
    parser.add_argument('input', help='Plik wejściowy')
    parser.add_argument('output', help='Plik wyjściowy')
    args = parser.parse_args()
    
    print(f"Konwertuję: {args.input} -> {args.output}")

if __name__ == "__main__":
    main()