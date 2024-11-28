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
            print(f'index Block {ind} is already allocated')
            return -1
        self.index_block=IndexBlock(ind)
        print(f'Index block {ind} is allocated')
        alloc.add(ind)
        return 0
    def allocdb(self,ind,alloc):
        if ind in alloc:
            print(f'Block {ind} is already allocated')
            return -1
        if not self.index_block:
            print(f'allocate index block first')
            return -1
        self.index_block.pointers.append(ind)
        print(f"Block {ind} is allocated ")
        alloc.add(ind)
        return 0
    def display(self):
        if not self.index_block:
            print(f"no blocks are allocated")
            return 
        print(f'Index block with {self.index_block.index} points to the data blocks ',end=" ")
        for ind in self.index_block.pointers:
            print(ind,end=" ")
        print()
def main():
    alloc=set()
    files=[]
    while True:
        fn=input("enter the file name: ")
        if fn.lower()=="exit":
            break
        file=IndexedFile(fn)
        ind_block=int(input(f"enter the index block for {fn}:"))
        if file.allocind(ind_block,alloc)==-1:
            continue
        ndb=int(input(f"enter the no. of data blocks for the {fn}"))
        for _ in range(ndb):
            dbi=int(input(f"enter the data block index for {fn}:"))
            while file.allocdb(dbi,alloc)==-1:
                dbi=int(input(f"enter the data block index for {fn}:"))
        files.append(file)
        print("current allocations")
        for f in files:
            f.display()
main()


