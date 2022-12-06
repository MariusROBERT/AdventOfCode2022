def test_sequence(i: int, input_seq: str, size: int):
    for j in input_seq[i:i + size]:
        if input_seq[i:i + size].count(j) > 1:
            return 0
    return 1


def get_sequence(input_seq: str, size: int):
    for i in range(len(input_seq)):
        if test_sequence(i, input_seq, size) == 1:
            return i + size


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read()
    start1 = get_sequence(content, 4)
    start2 = get_sequence(content, 14)
    print(f"Part 1 : {start1} ({content[start1 - 4:start1]})")
    print(f"Part 1 : {start2} ({content[start2 - 14:start2]})")

