def mru_page_replacement(pages, capacity):
    memory = []
    hits = 0
    misses = 0
    recent_page = None
    for i in range(len(pages)):
        if pages[i] in memory:
            hits += 1
        else:
            misses += 1
            if len(memory) < capacity:
                memory.append(pages[i])
            else:
                # Remove the most recently used page
                if recent_page in memory:
                    memory.remove(recent_page)
                memory.append(pages[i])
        recent_page = pages[i]  # Set the current page as the most recently used
        print(f"Step {i + 1}: Page {pages[i]}, Memory: {memory}")
    
    total_requests = len(pages)
    hit_ratio = hits / total_requests if total_requests > 0 else 0
    miss_ratio = misses / total_requests if total_requests > 0 else 0
    
    print(f"\nTotal page faults (misses): {misses}")
    print(f"Total hits: {hits}")
    print(f"Hit ratio: {hit_ratio:.2f}")
    print(f"Miss ratio: {miss_ratio:.2f}")

# User input
pages = list(map(int, input("Enter the pages (space-separated): ").split()))
frames = int(input("Enter the number of frames: "))
mru_page_replacement(pages, frames)
