import random
import matplotlib.pyplot as plt
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]



# values = random_numbers(10)  # 10 čísel v rozsahu 0–100
# print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
#
# small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20


def selection_sort(numbers):
    number = len(numbers)

    for i in range(number):
        min_index = i

        for j in range(i + 1, number):
            if numbers[j] < numbers[min_index]:
               min_index = j
        temp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = temp
    return numbers


# numbers = [5, 4, 1, 2, 8]
# number = len(numbers)
# for i in range(number):
#     min_index = i
#
#     for j in range(i + 1, number):
#         if numbers[j] < numbers[min_index]:
#            min_index = j
#     temp = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = temp
# print(numbers)


def bubble_sort(numbers):
    #numbers = [5, 4, 1, 2, 8]
    plt.ion()
    plt.show()
    numbers = [5, 4, 1, 2, 8]
    numbers = numbers.copy()
    number = len(numbers)

    for i in range(number):
        for j in range(0, number - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), number, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    # print(numbers)
    return numbers


# plt.ion()
# plt.show()
# numbers = [5, 4, 1, 2, 8]
# numbers = numbers.copy()
# number = len(numbers)
#
# for i in range(number):
#     for j in range(0, number - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#         index_highlight1 = j
#         index_highlight2 = j + 1
#         colors = ["steelblue"] * len(numbers)
#         colors[index_highlight1] = "tomato"
#         colors[index_highlight2] = "tomato"
#         plt.clf()
#         plt.bar(range(len(numbers)), number, color=colors)
#         plt.title("Bubble Sort")
#         plt.pause(0.1)
# plt.ioff()
# plt.show()
# print(numbers)


