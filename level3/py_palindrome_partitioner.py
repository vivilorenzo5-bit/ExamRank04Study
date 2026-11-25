def palindrome_partitioner(s: str) -> int:
    n = len(s)
    cuts = list(range(-1, n))
    for mid in range(n):
        for k, r in ((mid, mid), (mid, mid + 1)):
            while k >= 0 and r < n and s[k] == s[r]:
                cuts[r + 1] = min(cuts[r + 1], cuts[k] + 1)
                k -= 1
                r += 1
    return max(0, cuts[n])


print(palindrome_partitioner("abc"))
