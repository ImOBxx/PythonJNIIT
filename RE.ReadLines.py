import re

def find_lines_with_digits(file_path):
    with open(file_path, 'r') as file:
         lines = file.readlines()


    digit_pattern = re.compile(r'\d')
    

    line_numbers_with_digits = []
    

    for line_number, line in enumerate(lines, start=1):
        if digit_pattern.search(line):
            line_numbers_with_digits.append(line_number)
    
    return line_numbers_with_digits


file_path = 'TXT.txt'


lines_with_digits = find_lines_with_digits(file_path)
if lines_with_digits:
    print("Lines containing digits:", lines_with_digits)
else:
    print("No lines contain digits.")
