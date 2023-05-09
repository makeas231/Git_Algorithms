# Алгоритм Боера Мора
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = [m] * 256
    for i in range(m - 1):
        skip[ord(pattern[i])] = m - i - 1
    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(skip[ord(text[i])], m - j)
    return -1
