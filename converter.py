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

import json

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
