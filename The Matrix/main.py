TITLE = "The Matrix: THE GAME"
matrix = [["free robux","free vbucks"],["gubbys","cats"]]
print(len(matrix))
print(len(matrix[0]))
print(matrix[1][0])
for i in range (len(matrix)):
    for d in range (len(matrix[0])):
        print(matrix[i][d])
box = input("Enter Len(input)")
shelf = input("Enter Len(input[0])")
attic = []
for h in range(int(box)):
    closet = []
    for l in range(int(shelf)):
        conveyor = input("Enter List Items (ELI)")
        closet.append(conveyor)
    attic.append(closet)
print(attic)
Matrix_2 = [[1,2],[3,5]]
Matrix_3 = [[10,6],[7,8]]