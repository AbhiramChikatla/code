def lru(capacity,pages):
    hits=misses=hits_ratio=miss_ratio=0
    frames=[]
    lru=[]
    for i in range(len(pages)):
        if pages[i] in frames:
            hits+=1
            lru.remove(pages[i])
            lru.append(pages[i])
        else:
            misses+=1
            if len(frames)<capacity:
                frames.append(pages[i])
            else:
                ele=lru.pop(0)
                frames.remove(ele)
                frames.append(pages[i])
            lru.append(pages[i])

        print(f'Page : {pages[i]} , frames : {frames}')
    total_accesses=len(pages)
    hits_ratio=hits/total_accesses
    miss_ratio=misses/total_accesses
    return hits,misses,hits_ratio,miss_ratio


capacity=int(input("Enter the no of frames"))
pages=list(map(int,input("Enter the pages separated by space").split()))
hits,misses,hits_ratio,miss_ratio=lru(capacity,pages)
print("Total hits are: ", hits )
print("Total misses are: ", misses )
print("Hits ration are: ", hits_ratio )
print("Miss ration are: ", miss_ratio )