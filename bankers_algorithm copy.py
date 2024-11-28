def input_mat(rows,cols,name):
    print(f"Enter the {name} matrix : {rows} x {cols} :")
    matrix=[]
    for i in range(rows):
        while True:
            try:
                row=list(map(int,input().split(f"Enter the {i+1} row :").split()))
                if len(row)!=cols:
                    raise ValueError("please enter a correct one")
                matrix.append(row)
                break
            except ValueError:
                print(f"please enter {cols} integers separated by spaces:")
    return matrix
def find_ss(n,m,alloc,maxi,avail):
    need=[[maxi[i][j]-alloc[i][j] for j in range(m)] for i in range(n)]
    ind=0
    ans=[]
    f=[0]*n
    for _ in range(n):
        for i in range(n):
            if f[i]==0 and all(need[i][j]<=avail[j] for j in range(m)):
                ans.append(i)
                ind+=1
                f[i]=1
                for j in range(m):
                    avail[j]+=alloc[i][j]
                break
    return ans if ind==n else None

if __name__=="__main":
    n=int(input())
    m=int(input())
    alloc=input_mat(n,m,"alloc")
    maxi=input_mat(n,m,"maxi")
    avail=list(map(int,input().split()))
    safe=find_ss(n,m,alloc,maxi,avail)
    if safe is not None:
        print("following is the safe sequence")
        print("-> ".join(f"P{p}" for p in safe))
    else:
        print("No safe sequence found")