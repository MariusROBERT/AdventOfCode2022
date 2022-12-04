def part_one(a: tuple[str, str]):
    for item in a[0]:
        if item in a[1]:
            if item.islower():
                return ord(item) - ord('a') + 1
            else:
                return ord(item) - ord('A') + 27
    return 0


def part_two(a: str, b: str, c: str) -> int:
    for item in a:
        if item in b and item in c:
            if item.islower():
                return ord(item) - ord('a') + 1
            else:
                return ord(item) - ord('A') + 27
    return 0


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()
    bags1 = content.split("\n")
    bags2 = list()
    score1 = 0
    score2 = 0
    for bag in bags1:
        bags2.append((bag[:int(len(bag) / 2)], bag[int(len(bag) / 2):]))
    for bag in bags2:
        score1 += part_one(bag)
    for i in range(int(len(bags1) / 3)):
        score2 += part_two(bags1[i * 3], bags1[i * 3 + 1], bags1[i * 3 + 2])
    print(f"Part 1 : {score1}")
    print(f"Part 2 : {score2}")
