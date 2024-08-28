import re
import argparse

def read_replacements(file_path):
    replacements = []
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                replacements.append((key, value))
    return replacements

def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines

def replace_and_count(line, replacements):
    count = 0
    for old, new in replacements:
        replacements_count = line.count(old)
        count += replacements_count * len(old) 
        line = line.replace(old, new)
    return line, count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file')
    parser.add_argument('text_file')

    args = parser.parse_args()
    
    replacements = read_replacements(args.config_file)
    
    lines = read_lines(args.text_file)
    
    results = []

    for line in lines:
        modified_line, modified_count = replace_and_count(line, replacements)
        results.append((modified_line, modified_count))

    results.sort(key=lambda x: x[1], reverse=True)

    for modified_line, modified_count in results:
        print(f"Строка: {modified_line}, Замены: {modified_count}")

if __name__ == '__main__':
    main()