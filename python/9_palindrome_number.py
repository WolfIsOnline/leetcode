def isPalindrome(self, x: int) -> bool:
    x_str = str(x)
    index = len(x_str)
    final = ""
    for c in range(0, len(x_str)):
        index -= 1
        final = final + x_str[index]
    if final == str(x):
        return True
    return False