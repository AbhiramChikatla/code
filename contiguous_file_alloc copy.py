class Cont:
    def __init__(self,name,sb,len):
        self.name=name
        self.sb=sb
        self.length=len
    def display(self):
        print(f'File {self.name} is allocated from {self.sb} to {self.sb+self.length-1}')
def main():
    files=[]
    alloc=set()
    while True:
        fn=input("enter the file name: ")
        if fn.lower()=='exit':
            break
        sb=int(input("enter the starting block of the file "))
        length=int(input("enter the length of the file "))
        if any(block in alloc for block in range(sb,sb+length)):
            print("Error")
            continue
        for block in range(sb,sb+length):
            alloc.add(block)
        file =Cont(fn,sb,length)
        files.append(file)
        print("Current allocation are:")
        for f in files:
            f.display()
if __name__=="__main__":
    main()