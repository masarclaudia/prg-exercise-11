from sorting import random_numbers, selection_sort, bubble_sort


def main():
    numbers = [5, 1, 4, 2, 8]

    print("Pôvodný zoznam:\n", numbers)
    print()

    print("Selection sort:")
    print(selection_sort(numbers))
    print()

    print("Bubble sort:")
    print(bubble_sort(numbers))

    random_list = random_numbers(20)
    print()

    print("Náhodný zoznam:")
    print(random_list)
    print()

    print("Selection sort náhodného zoznamu:")
    print(selection_sort(random_list))
    print()

    print("Bubble sort náhodného zoznamu:")
    print(bubble_sort(random_list))


if __name__ == "__main__":
    main()