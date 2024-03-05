def bracket_checker(code):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for i, char in enumerate(code, start=1):
        if char in opening_brackets:
            stack.append((char, i))
        elif char in closing_brackets:
            if not stack or not is_matching(stack.pop()[0], char):
                return i

    if stack:
        return stack[0][1]
    else:
        return "Success"


def is_matching(opening, closing):
    return opening == '(' and closing == ')' or opening == '{' and closing == '}' or opening == '[' and closing == ']'


# Example usage:
code_input = input()
result = bracket_checker(code_input)

if result == "Success":
    print(result)
else:
    print(result)
