def fifo(pages,capacity):
    memory=[]
    hits=0
    misses=0
    for page in pages:
        if page in memory:
            hits+=1
        else:
            misses+=1
            if len(memory)==capacity:
                memory.pop(0)
            memory.append(page)
        print(f'Page:{page} Memory: {memory}')
    hit_ratio=hits/len(pages)
    miss_ratio=misses/len(pages)
    print(hits,misses,hit_ratio,miss_ratio)
pages=list(map(int,input().split()))
capacity=int(input())
fifo(pages,capacity)