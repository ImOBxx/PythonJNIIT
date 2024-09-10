l = list()
def invert_list(l):
 negated_list = [- x for x in l]
 print()
 print(negated_list)
 print()


while True:
  print()
  data = int (input ("Enter Number: "))
  l.append(data)
  print()
  x = input ("Do You Want To Continue (Y / N) : ")
  print()
  if (x == 'n'):
    break

invert_list(l) 

  


