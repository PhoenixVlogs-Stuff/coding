list1 = set(["Nita","Isabella","Huub","Neeltje","Sjors"])
list2 = set(["Huub","Nita","Carlijn","Awinita","Kai"])
list3 = set([])
list3 = list1 & list2
print(list3)
list3 = list1 ^ list2
print(list3)
list3 = list1 - list2
print(list3)