i = {"small_key": 0,"boss_key": 0, "bait": 0, "test": "test"} #1. integer 2. float 3. string 4. boolean = true or false
print(i)
i["bait"]+=5
print(i)
i["small_key"]+=7
i["boss_key"]+=1
print(i)
print(i.keys())
print(i.values())
for e in i:
    print(e,i[e])
if "bait" in i:
    print("bait exists")
else:
    print("crash... bait not present in dict i")
if "map" in i:
    print("Pirating is not allowed. Delete the file")
else:
    print("Pirating check completed! Real game. continue playing...")
i["island"]= "outset island"
print(i)
del(i["test"])
print(i)
i["cor"]=[0,78,0]
print(i)
print(i["cor"][1])