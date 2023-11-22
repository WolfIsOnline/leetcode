def lengthOfLastWord(self, s: str) -> int:
    s_r = "".join(reversed(s))
    l_d = False
    l_w = ""
    for l in s_r:
        if l.isspace() is True:
            if l_d is False:
                continue
            break
        elif l.isspace() is False and l_d is False:
            l_d = True
        l_w = l_w + l
    return len(l_w)