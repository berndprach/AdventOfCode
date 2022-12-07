
def read_input():
    with open("input.txt") as f:
        return f.read().splitlines()


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = {}
        self.subdirectoriers = {}
        self.calculated_size = None

    def __str__(self):
        return f"{self.name} ({self.get_size()})\n" \
               f"   Subdirs: {[sn for sn in self.subdirectoriers.keys()]}\n" \
               f"   Files: {[fn for fn in self.files.keys()]}"

    def add_file(self, file):
        self.files[file.name] = file

    def add_subdirectory(self, subdirectory):
        self.subdirectoriers[subdirectory.name] = subdirectory

    def calculate_size(self):
        self.calculated_size = 0
        for file in self.files.values():
            self.calculated_size += file.size
        for sub_dir in self.subdirectoriers.values():
            self.calculated_size += sub_dir.get_size()

    def get_size(self):
        if self.calculated_size is None:
            self.calculate_size()
        return self.calculated_size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def create_file_system(lines):
    root = Directory(name="root")
    current_dir = root
    all_directories = [root]
    for line in lines:
        if line == "$ cd /":
            current_dir = root
        elif line == "$ cd ..":
            current_dir = current_dir.parent
        elif line.startswith("$ cd "):
            subdir_name = line.replace("$ cd ", "")
            assert subdir_name in current_dir.subdirectoriers.keys()
            current_dir = current_dir.subdirectoriers[subdir_name]
        elif line == "$ ls":
            pass
        elif line.startswith("dir"):  # E.g. "dir a"
            dir_name = line.replace("dir ", "")
            if dir_name not in current_dir.subdirectoriers.keys():
                new_dir = Directory(name=dir_name, parent=current_dir)
                current_dir.add_subdirectory(new_dir)
                all_directories.append(new_dir)
        elif line[0].isdigit():  # E.g. "14848514 b.txt"
            file_size, file_name = line.split(" ")
            file_size = int(file_size)
            new_file = File(name=file_name, size=file_size)
            current_dir.add_file(new_file)
        else:
            raise ValueError(f"Unknown line: {line}")
    return root, all_directories


def solve(lines):
    solution = 0
    root, all_directories = create_file_system(lines)
    for directory in all_directories:
        dir_size = directory.get_size()
        if dir_size <= 100000:
            solution += dir_size
    return solution


def main():
    line = read_input()
    solution = solve(line)
    print(f"{solution = }")


if __name__ == "__main__":
    main()
