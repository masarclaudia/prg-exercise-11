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
#5

from hodnoceni_studentu import StudentsGrades
from sorting import random_numbers

# def main():
#     results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
#     print("Pocet studentov: ",len(results))
#     for i in range(len(results)):
#         print(f"Student {i}: {results[i]} points - {get_grade(self, i)}")
#
#     print("Plny pocet bodov")



def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Počet studentov:", results.count())
    print("------- známky -------")
    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

    print("----- Plný počet bodov (100 bodov) -----")
    print(results.get(100))

    print("---- plny pocet bodov (100 bodov) ----")
    print(results.find(100))

    print("---- zoradene výsledky ----")
    print(results.get_sorted())

    print()
    random_results = StudentsGrades(random_numbers(30, 0, 100))

    print("Počet študentov:", random_results.count())

    print("\n--- zoradené náhodné vysledky ---")
    print(random_results.get_sorted())


if __name__ == "__main__":
    main()