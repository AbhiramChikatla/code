def mru(pages,capacity):
    misses=hits=miss_ratio=hit_ratio=0
    recent_page=None
    memory=[]
    for page in pages:
        if page in memory:
            hits+=1
        else:
            misses+=1
            if len(memory)<capacity:
                memory.append(page)
            else:
                if recent_page in memory:
                    memory.remove(recent_page)
                memory.append(page)
        recent_page=page
    print(hits)
    print(misses)
    print(hit_ratio)
    print(miss_ratio)
pages = list(map(int, input("Enter the pages (space-separated): ").split()))
frames = int(input("Enter the number of frames: "))
mru(pages, frames)

    
