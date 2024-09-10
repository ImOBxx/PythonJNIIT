import re

def extract_domains(file_path):
   
    domains = set()
    
  
    domain_pattern = re.compile(r'//([^/]+)')
    

    with open(file_path, 'r') as file:
      
        lines = file.readlines()

    for line in lines:
  
        line = line.strip()
   
        match = domain_pattern.search(line)
        if match:
            
            domains.add(match.group(1))
    
    return list(domains)


file_path = 'TXT.txt'


unique_domains = extract_domains(file_path)
if unique_domains:
    print("Unique domains found in the file:")
    for domain in unique_domains:
        print(domain)
else:
    print("No domains found in the file.")
