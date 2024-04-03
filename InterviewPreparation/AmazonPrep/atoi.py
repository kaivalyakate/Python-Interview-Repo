def atoi(num_string: str) -> int:
    is_positive = True
    first_char = True
    result = ""
    for c in num_string:
        if c.isspace() and first_char: continue
        if c in ("-", "+") and first_char:
            first_char = False
            if c == "-": is_positive = False
        elif c.isnumeric():
            result += c
            first_char = False
        else: break

    if result == "": return 0
    result = "-" + result if not is_positive else result
    if int(result) >= (2**31) - 1:
        return ((2**31) - 1)
    elif int(result) <= -(2**31):
        return -(2**31)
    
    return int(result)


if __name__ == "__main__":
    print(atoi("+-123"))