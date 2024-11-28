def input_matrix(rows, cols, name):
    print(f"Enter the {name} matrix ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError("Invalid number of columns.")
                matrix.append(row)
                break
            except ValueError:
                print(f"Please enter {cols} integers separated by spaces.")
    return matrix

def find_safe_sequence(n, m, alloc, max_resources, avail):
    need = [[max_resources[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    f = [0] * n
    ans = []
    ind = 0

    for _ in range(n):
        for i in range(n):
            if f[i] == 0 and all(need[i][j] <= avail[j] for j in range(m)):
                ans.append(i)
                f[i] = 1
                for j in range(m):
                    avail[j] += alloc[i][j]
                ind += 1
                break

    return ans if ind == n else None

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    m = int(input("Enter the number of resources: "))
    alloc = input_matrix(n, m, "allocation")
    max_resources = input_matrix(n, m, "maximum")
    avail = list(map(int, input("Enter the available resources (space-separated): ").split()))

    safe_sequence = find_safe_sequence(n, m, alloc, max_resources, avail)
    if safe_sequence is not None:
        print("Following is the SAFE Sequence:")
        print(" -> ".join(f"P{p}" for p in safe_sequence))
    else:
        print("No safe sequence exists.")



