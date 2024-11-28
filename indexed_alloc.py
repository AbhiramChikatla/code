class File:
    def _init_(self, name):
        self.name = name
        self.index_block = []

class FileSystem:
    def _init_(self):
        self.files = []

    def create_file(self):
        # Get file name and number of blocks
        name = input("Enter file name: ")
        file = File(name)
        
        num_blocks = int(input(f"Enter the number of blocks for '{name}': "))
        print("Enter the block numbers:")
        
        # Collect unique block numbers and store in index block
        for i in range(num_blocks):
            while True:
                block_number = int(input(f"Block {i + 1}: "))
                if block_number not in file.index_block:
                    file.index_block.append(block_number)
                    break
                else:
                    print(f"Block {block_number} is already filled. Please enter a unique block number.")

        self.files.append(file)
        print(f"File '{name}' created with unique index block: {file.index_block}")

    def display_files(self):
        if not self.files:
            print("No files in the system.")
            return
        
        for file in self.files:
            print(f"File: {file.name}")
            print("Index Block:", file.index_block)
            print()

# Example usage
file_system = FileSystem()
num_files = int(input("Enter the number of files to create: "))
for _ in range(num_files):
    file_system.create_file()
file_system.display_files()