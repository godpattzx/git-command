def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    return numbers

if __name__ == "__main__":
    numbers = list(map(int, input("Enter integer numbers with space: ").split()))
    sorted_numbers = insertion_sort(numbers.copy())  # Make a copy to keep the original list unchanged
    print("Sorted numbers are:", sorted_numbers)
