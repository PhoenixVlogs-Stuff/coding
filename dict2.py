vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
print(vowels)
name = input("enter something - ")
for i in name:
    if i in vowels:
        vowels[i] += 1
print(vowels)
letters = {"q": 0, "w": 0, "e": 0, "r": 0, "t": 0, "y": 0, "u": 0, "i": 0, "o": 0, "p": 0, "a": 0, "s": 0, "d": 0, "f": 0, "g": 0, "h": 0, "j": 0, "k": 0, "l": 0, "z": 0, "x": 0, "c": 0, "v": 0, "b": 0, "n": 0, "m": 0}
for i in name:
    if i in letters:
        letters[i] += 1
print(letters)
count = {}
for i in name:
    if i.isalpha():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
print(count)
numbers = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
number = input("Enter a number: ")
for i in number:
    if i in numbers:
        numbers[i] += 1
check = True
for i in numbers.values():
    if i == 0:
        check = False
if check == True:
    print("Entered number is a panagram.")
else:
    print("Entered number is not a panagram.")
