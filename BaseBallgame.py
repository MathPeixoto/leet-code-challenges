def calPoints(ops) -> int:
    temp_record = []

    for c in ops:
        if c == "C":
            temp_record.pop()
        elif c == "D":
            double_record = int(temp_record[-1]) * 2
            temp_record.append(double_record)
        elif c == "+":
            first_number = int(temp_record[-1])
            second_number = int(temp_record[-2])
            temp_record.append(first_number + second_number)
        else:
            temp_record.append(c)

    result = sum(map(int, temp_record))

    return result


if __name__ == '__main__':
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]

    print(calPoints(ops))
