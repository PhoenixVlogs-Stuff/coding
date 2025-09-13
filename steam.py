class Steamlibrary:
    name = ""
    description = ""
    released = 1987
    developer = ""
    publisher = ""
    price = 0.0

    def __init__(self):
        print("add Steam game")
    
    def show_details(self):
        print(self.name)
        print(self.description)
        print(self.released)
        print(self.developer)
        print(self.publisher)
        print(self.price)
    
    def edit_details(self):
        self.name = input("Enter game name: ")
        self.description = input("Enter game description: ")
        self.released = int(input("Enter release year: "))
        self.developer = input("Enter developer name: ")
        self.publisher = input("Enter publisher name: ")
        self.price = float(input("Enter game price: "))

objectname = Steamlibrary()
objectname.edit_details()
objectname.show_details()