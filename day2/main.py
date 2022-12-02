if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()
    game = list()
    for line in content.split("\n"):
        game.append(line.split(" "))
    score = 0
    line = 0
    part2 = 0
    for match in game:
        if match[0] == "A":  # He play Rock
            if match[1] == "X":  # I play Rock
                score += 3 + 1
            elif match[1] == "Y":  # I play Paper
                score += 6 + 2
            elif match[1] == "Z":  # I play Scissors
                score += 3
        elif match[0] == "B":  # He play Paper
            if match[1] == "X":  # I play Rock
                score += 1
            elif match[1] == "Y":  # I play Paper
                score += 3 + 2
            elif match[1] == "Z":  # I play Scissors
                score += 6 + 3
        elif match[0] == "C":  # He play Scissors
            if match[1] == "X":  # I play Rock
                score += 6 + 1
            elif match[1] == "Y":  # I play Paper
                score += 2
            elif match[1] == "Z":  # I play Scissors
                score += 3 + 3

        if match[0] == "A":  # He play Rock
            if match[1] == "X":  # I play for to lose
                part2 += 3
            elif match[1] == "Y":  # I play to draw
                part2 += 3 + 1
            elif match[1] == "Z":  # I play to win
                part2 += 6 + 2
        elif match[0] == "B":  # He play Paper
            if match[1] == "X":  # I play for to lose
                part2 += 1
            elif match[1] == "Y":  # I play to draw
                part2 += 3 + 2
            elif match[1] == "Z":  # I play to win
                part2 += 6 + 3
        elif match[0] == "C":  # He play Scissors
            if match[1] == "X":  # I play for to lose
                part2 += 2
            elif match[1] == "Y":  # I play to draw
                part2 += 3 + 3
            elif match[1] == "Z":  # I play to win
                part2 += 6 + 1

    print(f"Part 1 : {score}")
    print(f"Part 2 : {part2}")

'''
A = rock
B = paper
C = scissors

X = rock
Y = paper
Z = scissors
'''
