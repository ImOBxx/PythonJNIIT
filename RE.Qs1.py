import re

def validate_url(url):
    
    pattern = re.compile(r'^(http://|https://)')
    
    if pattern.match(url):
        return True
    else:
        return False


url = input("Enter a URL: ")
if validate_url(url):
    print("The URL is valid.")
else:
    print("The URL is invalid.")
