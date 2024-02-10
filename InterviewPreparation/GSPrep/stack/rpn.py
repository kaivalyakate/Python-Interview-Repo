import math

def rpn(tokens: list[str]) -> int:
    stack = []        
    for token in tokens:
        if token in ("*", "/", "+", "-"):
            op2, op1 = stack.pop(), stack.pop()
            if token == "*": res = op1 * op2
            elif token == "/":
                res = op1 / op2
                if res > 0: res = math.floor(res)
                else: res = math.ceil(res)
            elif token == "+": res = op1 + op2
            elif token == "-": res = op1 - op2
            stack.append(res)
        else:
            stack.append(int(token))

    if stack != []: return stack[-1]
    return 0


if __name__ == "__main__":
    tokens = ["18"]
    print(rpn(tokens=tokens))
