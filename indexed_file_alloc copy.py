class IndexBlock:
    def __init__(self,index):
        self.index=index
        self.pointers=[]
class IndexedFile:
    def __init__(self,name):
        self.name=name 
        self.index_block=None
    def allocind(self,ind,alloc):
        if ind in alloc:
            print(f"block {ind} is already allocated")
            return -1
        self.index_block=IndexBlock(ind)
        alloc.add(ind)
        print(f' index block with index {self.index_block.index} is allocated')
        return 0
    def allocdata(self,ind,alloc):
        if ind in alloc:
            print(f"block {ind} is already allocated")
            return -1
        if not self.index_block:
            print("allocate index block first")
            return -1
        self.index_block.pointers.append(ind)
        alloc.add(ind)
        print(f' data block with index {ind} is allocated')
        return 0
    def display(self):
        if not self.index_block:
            print("No blocks are allocated")
            return -1
        print(f' index block with index {self.index_block.index} points to the data blocks with indexes',end=" ")
        for i in self.index_block.pointers:
            print(i ,end=" ")
        print()
        
def main():
    alloc=set()
    files=[]
    while True:
        fn=input("Enter the name fo the file: ")
        if fn.lower()=="exit":
            break
        ind_block=int(input("Enter the index block index"))
        file=IndexedFile(fn)
        if file.allocind(ind_block,alloc)==-1:
            continue
        ndb=int(input("Enter the no of data blocks"))
        for _ in range(ndb):
            dbi=int(input("Enter the index of data block"))
            while file.allocdata(dbi,alloc)==-1:
                dbi=int(input("Enter the index of valid data block"))
        files.append(file)
        print("current allocations")
        for f in files:
            f.display()
main()