import re

def find_all_numbers(file_path):
    
    numbers = []
    
    
    with open(file_path, 'r') as file:
        
        lines = file.readlines()
        
    
    number_pattern = re.compile(r'\b\d+\.?\d*\b')
    
    
    for line in lines:
       
        matches = number_pattern.findall(line)
        
        numbers.extend(matches)
    
    return numbers
file_path = 'TXT.txt'
all_numbers = find_all_numbers(file_path)
if all_numbers:
    print("Numbers found in the file:", all_numbers)
else:
    print("No numbers found in the file.")
