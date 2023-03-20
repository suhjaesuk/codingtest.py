def isValid(s):

    answer = "NO"
    stack=[]

    for p in s:
        if p=="(":
            stack.append(")")
        elif not stack or stack.pop() != p:
            return answer

    if not stack:
        answer="YES"

    return answer

