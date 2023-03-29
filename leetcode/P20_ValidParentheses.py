def isValid(str):
    stack = []
    for x in str:
        if x=='(':
            stack.append(')')
        elif x=='[':
            stack.append(']')
        elif x=='{':
            stack.append('}')
        elif not stack or stack.pop()!=x:
            return False

    if not stack:
        return True
    else:
        return False

str="{(([]))[]"
print(isValid(str))