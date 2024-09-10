import re

st = "smsdnsndende3456"
pattern = re.compile(r'[A-Za-z]')
print(pattern)
x = pattern.search(r'^[A-Za-z]')
print(x)
print(st[5:9])
if st == pattern:
    print("String Is Alphabetical")
else:
    print("String is Alphanumeric.")
