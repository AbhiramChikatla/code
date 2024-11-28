def lru(pages,capacity):
    memory=[]
    lru=[]
    hits=misses=hits_ratio_=misses_ratio=0
    for i in range(len(pages)):
        if pages[i] in memory:
            hits+=1
            lru.remove(pages[i])
            lru.append(pages[i])
        else:
            misses+=1
            if len(memory)<capacity:
                memory.append(pages[i])
            else:
                lru_page=lru.pop(0)
                memory.remove(lru_page)
                memory.append(pages[i])
            lru.append(pages[i])
        print(f'Page: {pages[i]} Memory: {memory}')
    hits_ratio=hits/len(pages)
    misses_ratio=misses/len(pages)
    print(hits)
    print(misses)
    print(hits_ratio)
    print(misses_ratio)
lru()
