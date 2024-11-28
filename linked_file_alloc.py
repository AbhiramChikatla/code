class Block:
    def __init__(self, index):
        self.index = index  # Index of the block
        self.next = None    # Pointer to the next block

class LinkedFile:
    def __init__(self, name):
        self.name = name
        self.head = None  # Head block of the linked list

    def allocate(self, index, allocated_blocks):
        """Allocate a block and link it to the file."""
        if index in allocated_blocks:
            print(f"Block {index} is already allocated.")
            return -1
        
        new_block = Block(index)
        if not self.head:
            self.head = new_block
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_block

        allocated_blocks.add(index)
        print(f"Block {index} allocated for '{self.name}'.")
        return 0

    def display(self):
        """Display the linked blocks of the file."""
        current = self.head
        if not current:
            print(f"No blocks allocated for '{self.name}'.")
            return

        print(f"Blocks allocated for '{self.name}':", end=" ")
        while current:
            print(current.index, end=" -> ")
            current = current.next
        print("None")

def main_linked():
    allocated_blocks = set()
    files = []

    while True:
        file_name = input("Enter the file name (or 'exit' to quit): ")
        if file_name.lower() == 'exit':
            break
        num_blocks = int(input(f"Enter the number of blocks to allocate for '{file_name}': "))

        file = LinkedFile(file_name)
        for _ in range(num_blocks):
            block_index = int(input(f"Enter block index for '{file_name}': "))
            while file.allocate(block_index, allocated_blocks) == -1:
                block_index = int(input("Enter a valid block index: "))

        files.append(file)

        # Display current allocations
        print("\nCurrent Allocations:")
        for f in files:
            f.display()

if __name__ == "__main__":
    main_linked()

