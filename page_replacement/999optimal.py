def optimal(pages,capacity):
    memory=[]
    hits=misses=0
    for i in range(len(pages)):
        if pages[i] in memory:
            hits+=1
        else:
            misses+=1
            if len(memory)<capacity:
                memory.append(pages[i])
            else:
                fp,fd=None,-1
                for j in memory:
                    if j not in pages[i+1:]:
                        fp=j
                        break
                    else:
                        fi=pages[i+1:].index(j)
                        if fi>fd:
                            fd=fi
                            fp=j
                if fp in memory:
                    memory.remove(fp)
                memory.append(pages[i])
        print(f'Page: {pages[i]} Memory: {memory}')
