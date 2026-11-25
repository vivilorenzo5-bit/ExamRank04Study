def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    rem = {p: {d for d in deps if d in packages} for p, deps in packages.items()}
    queue = sorted(p for p, deps in rem.items() if not deps)
    order = []
    while queue:
        curr = queue.pop(0)
        order.append(curr)
        ready = []
        for p, deps in rem.items():
            if curr in deps:
                deps.remove(curr)
                if not deps:
                    ready.append(p)
        queue.extend(sorted(ready))
    return order if len(order) == len(packages) else []
