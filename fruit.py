class fruit:
    name = ""
    color = ""

    def __init__(self):
        print("add fruit")
    
    def show_details(self):
        print(self.name)
        print(self.color)

    
    def edit_details(self):
        self.name = input("Enter fruit name: ")
        self.color = input("Enter fruit color: ")


objectname = fruit()
objectname.edit_details()
objectname.show_details()