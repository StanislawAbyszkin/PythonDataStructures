def is_balanced(string):
    stack = []
    open_bracket_dict = {'(': True, '{': True, '[': True}
    closed_bracket_dict = {')': '(', '}': '{', ']': '['}
    for char in string:
        if char in open_bracket_dict:
            stack.append(char)
        elif char in closed_bracket_dict:
            if not stack:
                return False
            if closed_bracket_dict[char] != stack.pop():
                return False

    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    print is_balanced('[](qwe){(())}asd')