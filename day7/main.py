DECAL = " "


class Element:
    def __init__(self, name: str, parent=None):
        self.__name = name
        self.__parent = parent

    @property
    def name(self):
        return self.__name

    @property
    def parent(self):
        return self.__parent


class File(Element):
    def __init__(self, name: str, size: int, parent: Element = None):
        super().__init__(name, parent)
        self.__name = name
        self.__parent = parent
        self.__size = size

    @property
    def size(self):
        return self.__size

    def print(self, decal: int = ""):
        print(decal * DECAL, end="")
        print(f"- {self.__name} (file, size={self.__size})")


class Folder(Element):
    def __init__(self, name: str, parent: Element = None):
        super().__init__(name, parent)
        self.__name = name
        self.__parent = parent
        self.__content = list()

    @property
    def content(self):
        return self.__content

    def add_elem(self, elem: Element):
        self.__content.append(elem)

    @property
    def size(self):
        size = 0
        for elem in self.__content:
            size += elem.size
        return size

    def get_file(self, name):
        for elem in self.__content:
            if type(elem) == File and elem.name == name:
                return elem
        return None

    def get_folder(self, name):
        for elem in self.__content:
            if type(elem) == Folder:
                if elem.name == name:
                    return elem
        return None

    def get_big_folders(self, size_min: int) -> list[int]:
        lst = list()
        for elem in self.__content:
            if type(elem) == Folder:
                lst += elem.get_big_folders(size_min)
                if elem.size >= size_min:
                    lst.append(elem.size)
        return lst

    def get_small_folders(self, size_max: int) -> list[int]:
        lst = list()
        for elem in self.__content:
            if type(elem) == Folder:
                lst += elem.get_small_folders(size_max)
                if elem.size <= size_max:
                    lst.append(elem.size)
        return lst

    def print(self, decal: int = 0):
        print(decal * DECAL, end="")
        print(f"- {self.__name} (dir, size={self.size})")
        for elem in self.__content:
            decal += 1
            if type(elem) == Folder:
                elem.print(decal)
            if type(elem) == File:
                elem.print(decal)

    def find_biggest_min(self, min_size: int):
        biggest = self
        for elem in self.__content:
            if type(elem) == Folder:
                tmp = elem.find_biggest_min(min_size)
                if min_size < tmp.size < biggest.size:
                    biggest = tmp
            if min_size < elem.size < biggest.size:
                biggest = elem
        return biggest


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()
    files = Folder("/")
    current = files
    lines = content.split("\n")
    for i in range(len(lines)):
        cmd = lines[i]
        arg = cmd.split(" ")
        if cmd.startswith("$ "):
            if cmd.startswith("$ cd"):
                if arg[2] == "..":
                    current = current.parent
                elif arg[2] == "/":
                    current = files
                else:
                    current = current.get_folder(arg[2])
            elif cmd.startswith("$ ls"):
                i += 1
                cmd = lines[i]
                while not cmd.startswith("$ "):
                    splitted = cmd.split(" ")
                    if splitted[0] == "dir":
                        current.add_elem(Folder(splitted[1], current))
                    else:
                        current.add_elem(File(splitted[1], int(splitted[0]), current))
                    i += 1
                    if i >= len(lines):
                        cmd = "$ "
                    else:
                        cmd = lines[i]
    # files.print()
    part1 = files.get_small_folders(100000)
    part2 = files.find_biggest_min(30000000 - (70000000 - files.size))
    print(f"Part 1:    {sum(part1)}")
    print(f"Part 2:    {part2.size}")

