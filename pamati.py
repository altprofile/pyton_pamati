import random

b = random.randint(1,11)
c = 3

for i in range(c):
  a = int(input("sk 1 - 10: "))
  if a == b:
    print("ir")
    break
  else:
    c = c -1
    print("nav bet tev ir", c, "meginajumi")