
import random

def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogosort(nums):                  # реализация алгоритма болотной сортировки
    while not is_sort(nums):
        random.shuffle(nums)
    return nums

numbers = list(range(10))
random.shuffle(numbers)              # перемешиваем начальный список
print(numbers)                       # выводим начальный список

sorted_numbers = bogosort(numbers)

print(sorted_numbers)   