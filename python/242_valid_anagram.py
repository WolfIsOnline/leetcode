def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    i = len(s)
    while i > 0:
        for x in t:
            try:
                if x == s[0]:
                    s = s.replace(x, "", 1)
                    t = t.replace(x, "", 1)
            except IndexError:
                pass
        if i == len(s):
            break
        i = len(s)
    if s == "":
        return True
    return False