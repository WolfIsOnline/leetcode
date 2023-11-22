def reverse(self, x: int) -> int:
    if x == 0:
        return 0
    s = str(x)
    length = len(s)
    result = ""
    while length > 0:
        length -= 1
        try:
            if s[length] == "0" and s[length - 1] == "0" and s[length + 1] == "0":
                continue
        except IndexError:
            continue
        if s[length] == "-":
            result = "-" + result
        else:
            result = result + s[length]
    if int(result) > 2147483647 or int(result) < -2147483647:
        return 0
    return int(result)