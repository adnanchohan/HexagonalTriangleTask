def is_core(a, b, c):
    # This function checks if there is a core cell in the triangular region
    # For simplicity, let's assume the core is the average of the three cells
    # This is a placeholder logic and should be replaced with actual core detection logic
    core = (a + b + c) // 3
    return core if core in (a, b, c) else None


def are_triangular(a, b, c):
    # This function checks if the cells form a triangular region
    # For simplicity, we will assume that if the sum of the smallest two is greater than the largest, they form a triangle
    return (a + b > c) and (a + c > b) and (b + c > a)


def process_sets(sets):
    results = []
    for a, b, c in sets:
        if are_triangular(a, b, c):
            core_cell = is_core(a, b, c)
            if core_cell is not None:
                results.append(core_cell)
            else:
                results.append(-1)  # No core found
        else:
            results.append(0)  # Not a triangular region
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