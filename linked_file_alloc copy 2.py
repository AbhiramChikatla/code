class Block:
    def __init__(self,ind):
        self.ind=ind 
        self.next=None
class LinkedFile:
    def __init__(self,name):
        self.name=name 
        self.head=None
    def allocate(self,ind,alloc):
        if ind in alloc:
            print(f'Block with {ind} is already allocated')
            return -1
        nb=Block(ind)
        ptr=self.head
        if not ptr:
            ptr=nb
        else:
            while ptr.next:
                ptr=ptr.next
            ptr.next=nb
        alloc.add(ind)
        print(f'Block with {ind} for file {self.name} is allocated successfully')
        return 0
    def display(self):
        ptr=self.head
        if not ptr:
            print(f'No blocks allocated for the file {self.name}')
            return 
        else:
            print(f'Blocks allocated for the file {self.name}',end=" ")
            while ptr:
                print(ptr.ind,end=" - >")
                ptr=ptr.next
            print("None")
def main():
    alloc=set()
    files=[]
    while True:
        fn=input("Enter the file name")
        if fn.lower()=="exit":
            break
        nb=int(input("Enter the no.of blocks"))
        file=LinkedFile(fn)
        for _ in range(nb):
            bi=int(input("Enter the block ind"))
            while file.allocate(bi,alloc)==-1:
                bi=int(input("Enter the valid block ind"))
        files.append(file)
        print("\n curren")
        for f in files:
            f.display()
main()