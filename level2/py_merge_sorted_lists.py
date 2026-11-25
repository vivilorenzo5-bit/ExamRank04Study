def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    q = [lst[:] for lst in lists if lst]
    while len(q) > 1:
        a, b = q.pop(0), q.pop(0)
        res, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        q.append(res + a[i:] + b[j:])
    return q[0] if q else []
