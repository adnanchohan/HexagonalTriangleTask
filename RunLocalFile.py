import datetime

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


def read_input_file(filename):
    sets = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                numbers = list(map(int, line.strip().split()))
                if len(numbers) == 3:
                    sets.append(tuple(numbers))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Invalid data in file. Ensure all values are integers.")
    return sets


def save_results_to_file(results):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{timestamp}.txt"
    with open(filename, 'w') as file:
        for i, result in enumerate(results, 1):
            file.write(f"{result}\n")
    print(f"Results saved to {filename}")


def main():
    input_data = []

    print("Enter inputs as comma-separated values (e.g., 1, 2, 3) or type 'file' to import a txt file.")
    print("Type 'done' to stop adding inputs and process the list.")

    while True:
        user_input = input("Enter three numbers (comma-separated), 'file' to import, or 'done' to process: ")

        if user_input.lower() == "done":
            break
        elif user_input.lower() == "file":
            filename = input("Enter the filename (e.g., input.txt): ")
            input_data.extend(read_input_file(filename))
        else:
            try:
                numbers = tuple(map(int, user_input.split(',')))
                if len(numbers) != 3:
                    print("Invalid input. Please enter exactly three numbers separated by commas.")
                    continue
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

    # Save results to file
    save_results_to_file(results)


if __name__ == "__main__":
    main()
