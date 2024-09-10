l = [5, 10, 8]
l2 = [2, 9, 7]

zip(l, l2)
list(zip(l, l2))

l = [5, 10, 8]
l2 = [2, 9, 7]

# Create a zip object
zipped = zip(l, l2)

# Convert the zip object to a list
zipped_list = list(zipped)
print(zipped_list)

for i in zip(l, l2):
    print(i)

l3 = [5, 6, 7, 8]
zipped = zip(l, l2, l3)
zipped_list = list(zipped)




