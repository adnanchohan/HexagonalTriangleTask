def is_core(a, b, c):
    # Sort the values to get the middle one as the core
    sorted_cells = sorted([a, b, c])
    core = sorted_cells[1]  # The middle value is considered the core in this case

    # Check if the difference between the largest and smallest values is small
    if sorted_cells[2] - sorted_cells[0] < 100:
        return 0
    return core


def are_triangular(a, b, c):
    # Check if the values form a valid triangle (sum of any two sides > the third)
    return (a + b > c) and (a + c > b) and (b + c > a)


def process_sets(sets):
    results = []
    for a, b, c in sets:
        if are_triangular(a, b, c):
            core_cell = is_core(a, b, c)
            results.append(core_cell)
        else:
            results.append(-1)  # Not a triangular region
    return results


def main():
    # Hardcoded input as specified in the requirements
    input_data = [
        (1, 2, 3),
        (2, 3, 1),
        (29, 20, 46),
        (277, 157, 139),
        (182, 188, 41),
        (100000000000000000000, 306, 103),
        (9240678, 7686199, 9240459)
    ]

    results = process_sets(input_data)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
