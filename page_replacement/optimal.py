def optimal_page_replacement(pages, capacity):
    memory = []
    hits = 0
    misses = 0
    
    for i in range(len(pages)):
        if pages[i] in memory:
            hits += 1
        else:
            misses += 1
            if len(memory) < capacity:
                memory.append(pages[i])
            else:
                # Find the page to be replaced (farthest in the future)
                farthest_page = None
                farthest_distance = -1
                for j in memory:
                    if j not in pages[i+1:]:
                        farthest_page = j
                        break
                    else:
                        future_index = pages[i+1:].index(j)
                        if future_index > farthest_distance:
                            farthest_distance = future_index
                            farthest_page = j
                # Remove the farthest page and insert the new page
                if farthest_page in memory:
                    memory.remove(farthest_page)
                memory.append(pages[i])
        
        print(f"Step {i + 1}: Page {pages[i]}, Memory: {memory}")
    
    total_requests = len(pages)
    hit_ratio = hits / total_requests if total_requests > 0 else 0
    miss_ratio = misses / total_requests if total_requests > 0 else 0
    
    print(f"\nTotal page faults (misses): {misses}")
    print(f"Total hits: {hits}")
    print(f"Hit ratio: {hit_ratio:.2f}")
    print(f"Miss ratio: {miss_ratio:.2f}")

# User input
capacity = int(input("Enter the number of frames: "))
pages = list(map(int, input("Enter the pages (space-separated): ").split()))
optimal_page_replacement(pages, capacity)
