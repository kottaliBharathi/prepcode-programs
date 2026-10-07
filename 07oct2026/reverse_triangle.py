for i in range(6,0,-1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end =" ")
    print()