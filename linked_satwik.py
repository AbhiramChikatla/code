# Initialize the blocks
f = [0] * 50

# Get the number of already allocated blocks
p = int(input("Enter how many blocks already allocated: "))
print("Enter blocks already allocated: ")

# Mark the allocated blocks
for i in range(p):
    a = int(input())
    f[a] = 1

while True:
    # Get starting block and length of the file to be allocated
    st = int(input("Enter index starting block: "))
    length = int(input("Enter index starting lenght: "))

    # Check if the starting block is free
    if f[st] == 0:
        for j in range(st, st + length):
            # If the block is free, allocate it
            if f[j] == 0:
                f[j] = 1
                print(f"{j} --------> {f[j]}")
            else:
                # If the block is already allocated, skip and increment length
                print(f"{j} Block is already allocated")
                length += 1
    else:
        print(f"{st} starting block is already allocated")

    # Ask if the user wants to allocate more files
    c = int(input("Do you want to enter more file (Yes - 1 / No - 0): "))
    if c == 0:
        break