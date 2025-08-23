import random
listed = set([7,7,3,3,5,5])
print(listed)
#also we are getting it in curly bracket
cnu = random.randint(0,9)
if cnu in listed:
    print(str(cnu) + " found, Continuing...")
else:
    print("Error: " + str(cnu) + " Not found. Please restart the device")
nnu = random.randint(4,9)
for i in range(nnu):
    i = random.randint(0,25)
    listed.add(i)
print(listed)
listed.remove(5)
print(listed)
listed.discard(25)
print(listed)
list1 = set([])
list2 = set([])
magiclist = set([])

for e in range(nnu):
    e = random.randint(0,9)
    list1.add(e)
for r in range(nnu):
    r = random.randint(0,9)
    list2.add(r)
print("")
magiclist = list1 | list2
print(list1)
print(list2)
print("")
print(magiclist)
print("")
magiclist = list1 & list2
print(magiclist)
print("")
magiclist = list1 - list2
print(magiclist)
print("")
magiclist = list1 ^ list2
print(magiclist)
print("")