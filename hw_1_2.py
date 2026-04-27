from collections import deque

def isPalindromeDeque(str: str):
    d = deque()
    # приводимо до одного регістру
    same_register_string = str.lower()
    # збираємо deque лише з alpha numeric
    for i in range(len(same_register_string)):
        candidate = same_register_string[i]
        if candidate.isalnum():
            d.append(candidate)

    left = 0
    right = len(d) - 1

    while left < right:
        leftSymbol = d.popleft()
        rightSymbol = d.pop()
        if leftSymbol != rightSymbol:
            return False
        left += 1
        right -= 1

    return True