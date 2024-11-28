# Initialize the block allocation array
f = [0] * 50

print("Files Allocated are:")

while True:
    count = 0
    # Get the starting block and the length of the file
    st = int(input("Enter starting block and length of files: "))
    length = int(input())

    # Check if there are enough free blocks
    for k in range(st, st + length):
        if f[k] == 0:
            count += 1

    # Allocate blocks if there are enough free blocks
    if length == count:
        for j in range(st, st + length):
            if f[j] == 0:
                f[j] = 1
                print(f"{j}\t{f[j]}")
        print("The file is allocated to disk")
    else:
        print("The file is not allocated")

    # Ask the user if they want to allocate more files
    c = int(input("Do you want to enter more files (Yes - 1 / No - 0): "))
    if c == 0:
        break
