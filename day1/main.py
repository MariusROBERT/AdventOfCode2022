if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()

    inventory = content.split("\n\n")
    elf = list()
    for item in inventory:
        elf.append(sum([int(i) for i in item.split("\n")]))
    print(f"Part 1 :\nElf carrying the most food carry {max(elf)} calories")

    elf.sort(reverse=True)
    print(f"\nPart 2 :\nTop 3 elf carrying the most food carry {sum(elf[0:3])} calories in total")
