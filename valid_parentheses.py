def is_valid(s: str) -> bool:
    # If is odd the parentheses are not valid.
    if len(s) % 2 != 0:
        return False

    pair_parentheses = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    # stack of open chars in the given string
    stack_parentheses = []

    # iterate over each character of the string
    for c in s:
        # if the char is in the pair parentheses, it means that is an open bracket
        if c in pair_parentheses:
            stack_parentheses.append(c)

        # if is not, so I need to compare the current char with the latest opened char from the stack
        else:

            # Get the latest opened char from stack
            if stack_parentheses:
                last_left_element = stack_parentheses.pop()

                # checking if the latest opened char is compatible with the current char. If it is, go to the next char
                if pair_parentheses[last_left_element] == c:
                    continue
                else:
                    return False
            else:
                return False

    return stack_parentheses == []


if __name__ == "__main__":
    line = '(){[]}'

    if is_valid(line):
        print("valid")

    else:
        print("invalid")
