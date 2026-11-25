def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    if dim <= 0:
        return []

    valid_stars = {
        (row, col)
        for row, col in stars
        if 0 <= row < dim and 0 <= col < dim
    }

    return [
        "".join("*" if (row, col) in valid_stars else "." for col in range(dim))
        for row in range(dim)
    ]
