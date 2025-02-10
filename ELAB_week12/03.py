def format_equations():
    equations = []
    while True:
        line = input()
        if line == "-1":
            break
        equations.append(line)

    max_len = max(len(eq.split("=")[0].strip()) for eq in equations)

    for eq in equations:
        left, right = eq.split("=", 1)
        left = left.strip()
        right = right.strip()
        print(" " * (max_len - len(left)) + left + " = " + right)

format_equations()