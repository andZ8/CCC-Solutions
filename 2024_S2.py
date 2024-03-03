# 15/15 Contest Day solution
n, length = input().split()
n = int(n)
length = int(length)
dict = {}
alternate = True
prev = ""
alpha = "abcdefghijklmnopqrstuvwxyz"

# loop for each of the test cases
for i in range(n):
  string = input()
  for i in alpha:
    if i in string:
      #assign each letter a dictionary key to keep count
      dict[i] = string.count(i)
  for i in string:
    # if i is the first letter (prev is blank) determine whether i is a "heavy" or "light" letter and set prev as either
    if prev == "":
      if dict[i] > 1:
        prev = "heavy"
      else:
        prev = "light"
    # if prev exists already, determine if i follows the order
    elif prev == "heavy":
      if dict[i] > 1:
        alternate = False
      else:
        prev = "light"
    else:
      if dict[i] <= 1:
        alternate = False
      else:
        prev = "heavy"
        
  if alternate:
    print("T")
  else:
    print("F")
  alternate = True
  prev = ""
  
