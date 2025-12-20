def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        left = alpha[size-1 : size-1-i : -1]
        right = alpha[size-1-i : size]
        row = "-".join(left + right)
        width = 4*size - 3
        lines.append(row.center(width, "-"))

    print("\n".join(lines + lines[-2::-1]))

