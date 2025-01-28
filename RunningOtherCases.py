def is_core(a, b, c):
    # Sort the values to get the middle one as the core
    sorted_cells = sorted([a, b, c])
    core = sorted_cells[1]  # The middle value is considered the core in this case

    # Check if the difference between the largest and smallest values is small
    if sorted_cells[2] - sorted_cells[0] < 100:
        return -1
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
            results.append(0)  # Not a triangular region
    return results


def main():
    input_data = []

    print("Enter inputs as comma-separated values (e.g., 1, 2, 3).")
    print("After entering an input, you can choose to process the list or add more inputs.")
    print("Type 'done' to stop adding inputs and process the list.\n")

    while True:
        user_input = input("Enter three numbers (comma-separated) or type 'done' to process: ")

        if user_input.lower() == "done":
            break

        try:
            # Parse the input into a tuple of three integers
            numbers = tuple(map(int, user_input.split(',')))

            if len(numbers) != 3:
                print("Invalid input. Please enter exactly three numbers separated by commas.")
                continue

            # Add the parsed input to the list
            input_data.append(numbers)

        except ValueError:
            print("Invalid input. Please enter valid integers separated by commas.")

    if not input_data:
        print("No input provided. Exiting.")
        return

    # Process the inputs
    results = process_sets(input_data)
    print("\nProcessing Results:")
    for i, result in enumerate(results, 1):
        print(f"Set {i}: {result}")


if __name__ == "__main__":
    main()
