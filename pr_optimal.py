def optimal(pages, capacity):
    memory = []  # to store pages in memory (fixed capacity)
    hits = 0
    misses = 0

    for i in range(len(pages)):
        if pages[i] in memory:
            # Page hit
            hits += 1
        else:
            # Page miss
            misses += 1
            if len(memory)< capacity:
                memory.append(pages[i])
            else:
                farthest_page =None
                farthest_distance=-1
                for j in memory:
                    if j not in pages[i+1:]:
                        farthest_page=j
                        break
                    else:
                        future_ind=pages[i+1:].index(j)
                        if future_ind>farthest_distance:
                            farthest_distance=future_ind
                            farthest_page=j
                if farthest_page in memory:
                    memory.remove(farthest_page)
                memory.append(pages[i])
    


            

        # For debugging purposes: printing memory status after each page
        print(f"Page: {pages[i]}, Memory: {memory}")

    # Calculating hit ratio and miss ratio
    total_accesses = len(pages)
    hit_ratio = hits / total_accesses
    miss_ratio = misses / total_accesses

    # Return hits, misses, hit ratio, and miss ratio
    return hits, misses, hit_ratio, miss_ratio


# Example usage
# Taking the capacity (number of frames)
capacity = int(input("Enter number of frames: "))
pages = list(map(int,input("Enter the pages separated by spaces: ").split()))

hits, misses, hit_ratio, miss_ratio = optimal(pages, capacity)
print(f"Total Hits: {hits}")
print(f"Total Misses: {misses}")
print(f"Hit Ratio: {hit_ratio:.2f}")
print(f"Miss Ratio: {miss_ratio:.2f}")
