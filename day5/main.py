from copy import deepcopy

if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()
    stacks_raw, instructions = content.split("\n\n")
    stacks = [list() for i in range(9)]
    stacks_raw_lines = stacks_raw.split("\n")
    for row in range(len(stacks_raw_lines) - 1):
        for column in range(len(stacks_raw_lines[row])):
            if stacks_raw_lines[row][column].isalpha():
                stacks[int(column / 4)].append(stacks_raw_lines[row][column])
    [stack.reverse() for stack in stacks]
    stacks2 = deepcopy(stacks)
    for instruction in instructions.split("\n"):
        words = instruction.split(" ")
        stack_to = int(words[5]) - 1
        stack_from = int(words[3]) - 1
        stack_iter = int(words[1])
        for i in range(stack_iter):
            stacks[stack_to].append(stacks[stack_from].pop())
        stacks2[stack_to] += stacks2[stack_from][-stack_iter:]
        for i in range(stack_iter):
            stacks2[stack_from].pop()
    print("Part 1 : ", end="")
    for stack in stacks:
        print(stack[len(stack) - 1], end="")
    print()
    print("Part 2 : ", end="")
    for stack in stacks2:
        print(stack[len(stack) - 1], end="")
    print()
