def palindrome_partitioner(s: str) -> int:
    n = len(s)
    cuts = list(range(-1, n))
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                cuts[j] = min(cuts[j], cuts[i] + 1)
    return max(0, cuts[n])
