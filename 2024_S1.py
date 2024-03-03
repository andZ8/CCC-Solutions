# Contest day 15/15
n = int(input())
count = 0
people = []
for i in range(n):
  people.append(int(input()))
# check if people sitting opposite have the same number
for i in range(n//2): #don't need to go all the way, halfway is enough
  if people[i] == people[i+(n//2)]:
    c += 2 
print(c)
