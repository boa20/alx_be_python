size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for j in range(1, size+1):
        print("*", end="")
    
    print("\n")
    row += 1