1
# words = ['ало', 'арбуз', 'телефон', 'нота', 'север']
# wordlens = list(map(len, words))
# my_list = []
# print('my_list:', list(map(lambda x: len(x),words[0:5])))
# print(words)
# print(min(wordlens)+max(wordlens))

2
# numbers = [2, 3, 4, 5, 6, 7]
# x_min = min(numbers)
# x_max = max(numbers)
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i]*=x_min
#     else:
#         numbers[i]*=x_max
# print("Максимальный элемент: ", x_max)
# print("Минимальный элемент: ", x_min)
# print(numbers)

3
# import random
#
# def random_generator(n):
#     lst_random = []
#     for i in range(n):
#         lst_random.append(random.uniform(-10.0, 10.0))
#     return lst_random
#
# if __name__ == "__main__":
#     n = int(input("n = "))
#     n_min = float(input("n_min = "))
#     n_max = float(input("n_max = "))
#     if n < 1 or n_min >= n_max:
#         print("ERROR: invalid input")
#     else:
#         count = 0
#         lst_random = random_generator(n)
#         print("lst_random : ", *lst_random)
#         for num in lst_random:
#             if num >= n_min and num < n_max:
#                 count += 1
#         print("count = ", count)

4
# if __name__ == "__main__":
#     lst_numbers = list(map(int, input().split()))
#     if len(lst_numbers) < 4:
#         print("ERROR: invalid count of numbers")
#     else:
#         lst_no_extremum = lst_numbers
#         lst_no_extremum.remove(max(lst_numbers))
#         lst_no_extremum.remove(min(lst_numbers))
#         print("new number list", *lst_numbers)

5
# if __name__ == "__main__":
#     n = int(input("number of sailors = "))
#     if n < 2:
#         print("ERROR: invalid count of sailors")
#     else:
#         team1 = []
#         team2 = []
#         print("enter sailors info:")
#         for i in range(n):
#             sailor = input()
#             [name] = [s for s in sailor.split() if not s.isdigit()]
#             [age] = [int(s) for s in sailor.split() if s.isdigit()]
#             if age > 40 or age < 20:
#                 team1.append(name)
#             else:
#                 team2.append(name)
#         print("team 1:", *team1)
#         print("team 2:", *team2)

6
n = int(input("Введите количество моряков: "))
team1 = []
team2 = []
for i in range(n):
    nameage = input().split()
    name = nameage[0]
    age = int(nameage[1])
    if age > 40 or age < 20:
        team1.append(name)
    else:
        team2.append(name)

team1.sort()
team2.sort()

print("Команда 1:", end=' ')
print(*team1, sep=', ')

print("Команда 2:", end=' ')
print(*team2, sep=', ')