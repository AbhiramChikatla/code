def fifo(capacity,pages):
    hits=misses=hits_ratio=miss_ratio=0
    memory=[]
    for page in pages:
        if page in memory:
            hits+=1
        else:
            misses+=1
            if len(memory)==capacity:
                memory.pop(0)
            memory.append(page)
        print(f'Page : {page} , Memory : {memory}')
    total_accesses=len(pages)
    hits_ratio=hits/total_accesses
    miss_ratio=misses/total_accesses
    return hits,misses,hits_ratio,miss_ratio


capacity=int(input("Enter the no of frames"))
pages=list(map(int,input("Enter the pages separated by space").split()))
hits,misses,hits_ratio,miss_ratio=fifo(capacity,pages)
print("Total hits are: ", hits )
print("Total misses are: ", misses )
print("Hits ration are: ", hits_ratio )
print("Miss ration are: ", miss_ratio )