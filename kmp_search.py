"Алгоритм поиска подстроки в строке с помощью алгоритма Кнута-Морриса-Пратта"
def kmp_search(string, pattern):
    n = len(string)
    m = len(pattern)
    lps = [0] * m
    j = 0
    compute_lps(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == string[i]:
            i += 1
            j += 1
        if j == m:
            return i-j
        elif i < n and pattern[j] != string[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1

def compute_lps(pattern, m, lps):
    len_longest_prefix_suffix = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[len_longest_prefix_suffix]:
            len_longest_prefix_suffix += 1
            lps[i] = len_longest_prefix_suffix
            i += 1
        else:
            if len_longest_prefix_suffix != 0:
                len_longest_prefix_suffix = lps[len_longest_prefix_suffix-1]
            else:
                lps[i] = 0
                i += 1
