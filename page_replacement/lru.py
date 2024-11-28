def lru_page_replacement(pages, capacity):
    frame = []
    lru = []  # List to track the order of usage
    hits = 0
    misses = 0
    
    for i in range(len(pages)):
        if pages[i] in frame:  # Page hit
            hits += 1
            # Move the page to the most recently used position
            lru.remove(pages[i])
            lru.append(pages[i])
        else:  # Page miss
            misses += 1
            if len(frame) < capacity:  # If there's space in the frame
                frame.append(pages[i])
            else:  # No space, replace the least recently used page
                lru_page = lru.pop(0)
                frame.remove(lru_page)
                frame.append(pages[i])
            # Add the new page to the usage list
            lru.append(pages[i])
        
        print(f"Step {i + 1}: Page {pages[i]} -> Frame: {frame}")
    
    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)
    
    return hits, misses, hit_ratio, miss_ratio

# Taking the capacity (number of frames)
capacity = int(input("Enter number of frames: "))

# Taking user input in a single line for pages
pages = list(map(int, input("Enter the pages separated by spaces: ").split()))


# Function call
hits, misses, hit_ratio, miss_ratio = lru_page_replacement(pages, capacity)

# Output results
print(f"\nTotal Hits: {hits}")
print(f"Total Misses: {misses}")
print(f"Hit Ratio: {hit_ratio:.2f}")
print(f"Miss Ratio: {miss_ratio:.2f}")
