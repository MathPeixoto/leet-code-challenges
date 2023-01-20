def calPoints(s) -> int:

    mapOcurrences = {}
    highestOccurence = 0
    highestChar = ''

    for c in s:
        if c.isalpha():
            if c not in mapOcurrences:
                mapOcurrences[c] = 1
            else:
                mapOcurrences[c] += 1

            if mapOcurrences[c] > highestOccurence:
                highestOccurence = mapOcurrences[c]
                highestChar = c

    return highestChar


if __name__ == '__main__':
    s = "fjdjgfk1234fgsdfigAAAAA"

    print(calPoints(s))
