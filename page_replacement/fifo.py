def fifo_page_replacement(pages, capacity):
    memory = []  # to store pages in memory (fixed capacity)
    hits = 0
    misses = 0

    for page in pages:
        if page in memory:
            # Page hit
            hits += 1
        else:
            # Page miss
            misses += 1
            if len(memory) == capacity:
                # If memory is full, remove the first page (FIFO)
                memory.pop(0)
            # Add the new page to memory
            memory.append(page)

        # For debugging purposes: printing memory status after each page
        print(f"Page: {page}, Memory: {memory}")

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

hits, misses, hit_ratio, miss_ratio = fifo_page_replacement(pages, capacity)
print(f"Total Hits: {hits}")
print(f"Total Misses: {misses}")
print(f"Hit Ratio: {hit_ratio:.2f}")
print(f"Miss Ratio: {miss_ratio:.2f}")
