if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()
    pairs = list()
    for line in content.split("\n"):
        (first, second) = line.split(",")
        pairs.append((first.split("-"), second.split("-")))
    score1 = 0
    score2 = 0
    for i in pairs:
        if int(i[0][0]) >= int(i[1][0]) and int(i[0][1]) <= int(i[1][1]):
            score1 += 1
        elif int(i[0][0]) <= int(i[1][0]) and int(i[0][1]) >= int(i[1][1]):
            score1 += 1

        if int(i[0][0]) in range(int(i[1][0]), int(i[1][1]) + 1):
            score2 += 1
        elif int(i[0][1]) in range(int(i[1][0]), int(i[1][1]) + 1):
            score2 += 1
        elif int(i[1][0]) in range(int(i[0][0]), int(i[0][1]) + 1):
            score2 += 1
        elif int(i[1][1]) in range(int(i[0][0]), int(i[0][1]) + 1):
            score2 += 1

    print(f"Part 1 : {score1}")
    print(f"Part 2 : {score2}")
