def char_occurrence(s) -> int:

    map_occurrences = {}
    highest_occurrence = 0
    highest_char = ''

    for c in s:
        if c.isalpha():
            if c not in map_occurrences:
                map_occurrences[c] = 1
            else:
                map_occurrences[c] += 1

            if map_occurrences[c] > highest_occurrence:
                highest_occurrence = map_occurrences[c]
                highest_char = c

    return highest_char


if __name__ == '__main__':
    str_example = "fjdjgfk1234fgsdfigAAAAA"

    print(char_occurrence(str_example))
