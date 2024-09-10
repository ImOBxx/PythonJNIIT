import re

f1 = open('Total___of_classes_20240614.csv')

for line in f1:
    rno = re.search(r"\d{3}", line)
    marks = re.findall(r"d{2}")
    print(rno.group())