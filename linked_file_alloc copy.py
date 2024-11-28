class Block:
    def __init__(self,ind):
        self.index=ind
        self.next=None

class LinkedFile:
    def __init__(self,name):
        self.name=name
        self.head=None
    def allocate(self,bi,alloc):
        if bi in alloc:
            print("block already allocated")
            return -1
        else:
            nb=Block(bi)
            if not self.head:
                self.head=nb
            else:
                cur=self.head
                while cur.next:
                    cur=cur.next
                cur.next=nb
            alloc.add(bi)
            print(f"block {bi} allocated for {self.name}")
        return 0
    def display(self):
        if not self.head:
            print("no block allocated")
        else:
            cur=self.head
            print(f"block allocation for {self.name}: " ,end=" ")
            while cur:
                print(f' {cur.index}' ,end=" -> ")
                cur=cur.next
            print("None")

def main():
    alloc=set()
    files=[]
    while True:
        fn=input("enter the name fo the file")
        if fn.lower()=='exit':
            break
        file=LinkedFile(fn)
        nb=int(input("enter the no of blocks"))
        for _ in range(nb):
            bi=int(input("Enter the block index"))
            while file.allocate(bi,alloc)==-1:
                bi=int(input("Enter the valid block index"))
        files.append(file)
        print("current block allocation")
        for f in files:
            f.display()
        

main()
        


    