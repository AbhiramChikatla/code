class ContiguousFile:
    def __init__(self, name, start_block, length):
        self.name = name
        self.start_block = start_block  # Starting block index
        self.length = length            # Number of blocks allocated

    def display(self):
        """Display the blocks allocated to the file."""
        print(f"File '{self.name}' is allocated from block {self.start_block} to block {self.start_block + self.length - 1}")

def main_contiguous():
    allocated_blocks = set()
    files = []

    while True:
        file_name = input("Enter the file name (or 'exit' to quit): ")
        if file_name.lower() == 'exit':
            break
        start_block = int(input(f"Enter the starting block for '{file_name}': "))
        length = int(input(f"Enter the number of blocks for '{file_name}': "))

        # Check if the blocks are free
        if any(block in allocated_blocks for block in range(start_block, start_block + length)):
            print(f"Error: Some of the blocks from {start_block} to {start_block + length - 1} are already allocated.")
            continue

        # Allocate the blocks
        for block in range(start_block, start_block + length):
            allocated_blocks.add(block)

        file = ContiguousFile(file_name, start_block, length)
        files.append(file)

        # Display current allocations
        print("\nCurrent Allocations:")
        for f in files:
            f.display()

if __name__ == "__main__":
    main_contiguous()
