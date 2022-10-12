1
# print("Введите коллицество минут, израсходованных в этом месяце")
# m = int(input())
# print("Введите коллицество смс-сообщений, израсходованных в этом месяце")
# c = int(input())
# print('Базовая сумма тарификации - 150 руб')
# m1 = 0
# c1 = 0
# if m > 50:
#     m1 = (m - 50)*2.5
# if c > 50:
#     c1 = (c - 50)*1.5
# if m1 + c1 != 0:
#     print('Сумма за дополнительные минуты минуты и сообщения -', format(m1 + c1, '.2f'), 'руб')
# print('Сумма отчислений кол-центрам - 4,4 руб')
# print('Налог - ', format((150 + m1 + c1 + 4.4)*0.05, '.2f'), 'руб')
# print('Итоговая сумма к оплате - ', format((150 + m1 + c1 + 4.4)*1.05, '.2f'), 'руб')

2
# v = int(input())
# if 0 < v <= 7.8:
#     print(0)
# if 7.8 < v < 11.2:
#     print(1)
# if 11.2 <= v <= 16.4:
#     print(2)
# if v > 16.4:
#     print(3)
# if v <= 0:
#     print('error')

3

# s = input()
# if len(s) >= 3:
#     if s[-3:] == 'ing':
#         print(s[0:-3] + 'ly')
#     else:
#         print(s + 'ing')
# else:
#     print(s)

4
# s = input()
# if s.find('@') != -1:
#     print(s[s.index('@')+1:])
# else:
#     print(s)s = input()

5
# s = input()
# while s.find(':') != -1:
#     s = s.replace(':', '.')
# while s.find('.') != -1 or s.find(',') != -1 or s.find('-') != -1 or s.find('!') != -1 or s.find('?') != -1:
#     s = s.replace('.', ':)')
#     s = s.replace(',', ':)')
#     s = s.replace('-', ':)')
#     s = s.replace('!', ':)')
#     s = s.replace('?', ':)')
# print(s)

6
# print('Введите название фрукта')
# a = input()
# print('Введите объем упаковки')
# b = input()

7
pin = input()
print(len(pin) == 4 or len(pin) == 6)




