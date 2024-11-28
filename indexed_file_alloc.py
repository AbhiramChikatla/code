class IndexBlock:
    def __init__(self, index):
        self.index = index  # Index of the index block
        self.pointers = []  # List of data block indexes

class IndexedFile:
    def __init__(self, name):
        self.name = name
        self.index_block = None  # Index block of the file

    def allocate_index_block(self, index, allocated_blocks):
        if index in allocated_blocks:
            print(f"Index block {index} is already allocated.")
            return -1
        self.index_block = IndexBlock(index)
        allocated_blocks.add(index)
        print(f"Index block {index} allocated for '{self.name}'.")
        return 0

    def allocate_data_block(self, index, allocated_blocks):
        if index in allocated_blocks:
            print(f"Data block {index} is already allocated.")
            return -1
        if not self.index_block:
            print("Allocate an index block first.")
            return -1
        self.index_block.pointers.append(index)
        allocated_blocks.add(index)
        print(f"Data block {index} allocated for '{self.name}'.")
        return 0

    def display(self):
        if not self.index_block:
            print(f"No index block allocated for '{self.name}'.")
            return
        print(f"Index block {self.index_block.index} for '{self.name}' points to data blocks:", end=" ")
        for index in self.index_block.pointers:
            print(index, end=" ")
        print()

def main_indexed():
    allocated_blocks = set()
    files = []

    while True:
        file_name = input("Enter the file name (or 'exit' to quit): ")
        if file_name.lower() == 'exit':
            break
        index_block = int(input(f"Enter index block for '{file_name}': "))
        file = IndexedFile(file_name)
        
        if file.allocate_index_block(index_block, allocated_blocks) == -1:
            continue

        num_data_blocks = int(input(f"Enter the number of data blocks to allocate for '{file_name}': "))
        for _ in range(num_data_blocks):
            data_block = int(input(f"Enter data block index for '{file_name}': "))
            while file.allocate_data_block(data_block, allocated_blocks) == -1:
                data_block = int(input("Enter a valid data block index: "))

        files.append(file)

        # Display current allocations
        print("\nCurrent Allocations:")
        for f in files:
            f.display()

if __name__ == "__main__":
    main_indexed()

