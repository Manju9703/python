
row = int(input("Enter the number of rows: "))

for i in range(row, 0, -1):
   
    for j in range(1, row - i + 1):
        print(" ", end = "")
    
    for j in range(1, 2 * i):
        print("*", end = "")
    
    print("")




