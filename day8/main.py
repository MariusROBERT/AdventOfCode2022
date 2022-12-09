class Forest:
    def __init__(self, raw: str):
        self.__map = raw.split("\n")
        self.__visiblemap = self.__init_visible()
        self.__visible = sum([i.count(True) for i in self.__visiblemap])

    @property
    def visible(self) -> int:
        return self.__visible

    def __init_visible(self) -> list[list[bool]]:
        tmp = [[False for _ in range(len(self.__map[0]))] for _ in range(len(self.__map))]
        test = 0
        for x in range(len(self.__map)):
            highest_left = 0
            highest_top = 0
            highest_right = 0
            highest_bot = 0
            for y in range(len(self.__map[x])):
                if x == 0 or y == 0 or y == len(self.__map[x]) - 1 or x == len(self.__map) - 1:
                    tmp[x][y] = True
                    test += 1
                if int(self.__map[y][x]) > highest_left:
                    tmp[y][x] = True
                    highest_left = int(self.__map[y][x])
                    test += 1
                if int(self.__map[y][-x - 1]) > highest_right:
                    tmp[y][-x - 1] = True
                    highest_right = int(self.__map[y][-x - 1])
                    test += 1
                if int(self.__map[x][y]) > highest_top:
                    tmp[x][y] = True
                    highest_top = int(self.__map[x][y])
                    test += 1
                if int(self.__map[x][-y - 1]) > highest_bot:
                    tmp[x][-y - 1] = True
                    highest_bot = int(self.__map[x][-y - 1])
                    test += 1
        for i in tmp:
            print(i)
        print(test)
        return tmp


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()
    forest = Forest(content)
    visible = forest.visible
    print(f"Part1: {visible}")
