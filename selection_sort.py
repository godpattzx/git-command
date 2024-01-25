def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers

if __name__ == "__main__":
    numbers = list(map(int, input("Enter integer numbers with space: ").split()))
    sorted_numbers = selection_sort(numbers.copy())  # Make a copy to keep the original list unchanged
    print("Sorted numbers are:", sorted_numbers)
