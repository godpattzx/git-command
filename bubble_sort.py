def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

if __name__ == "__main__":
    numbers = list(map(int, input("Enter integer numbers separated by space: ").split()))
    sorted_numbers = bubble_sort(numbers.copy())  
    print("Sorted numbers are:", sorted_numbers)
