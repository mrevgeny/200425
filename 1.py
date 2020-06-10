# # форматирование строк
# # my_name = 'Evgeny'
# # print('Hello   ' +  my_name)
# #
# # print('I have {}, {} {}'.format('delicios', 'red', 'apple'))
# # print('I have {0}, {2} {1}'.format('delicios', 'red', 'apple'))
# #
# # result = 100/777
# # print(result)
# # print('Результат: {r:1.5f} '. format(r=result))
# # print(f'Имя: {my_name}')
# # #____________________________
# #
# # Списки - List
# # my_list = [1, 2, 3]
# # my_list = ['string', 100, 23.3]
# # len(my_list)
# # print(my_list)
# # print(len(my_list))
# # print(my_list[0])
# # an_list = [4, 5]
# # print(my_list + an_list)
# # new_list = my_list + an_list
# # print(new_list)
# # new_list[0] = 'one'
# # print(new_list)
# # new_list.append(7)
# # print(new_list)
# # new_list.pop()
# # print(new_list)
# # pop_item = new_list.pop()
# # print(new_list)
# # new_list.pop(0)
# # print(new_list)
# # new_list = ['a', 'v', 'c', 'g', 'R']
# # new_list.sort()
# # my_sort = new_list
# # print(my_sort)
# # my_list.reverse()
# # print(new_list)
# #
# # # Dictionaries
# # dict = {'key1': 'value1', 'key2': 'value2'}
# # print(dict)
# # print(dict['key1'])
# # price = {'apple': 1.99, 'milk': 0.80}
# # print(price['apple'])
# # d = {'k1': 123, 'k2': [0, 1, 2]}
# # print(d['k2'][1])
# # d['k3'] = 300
# # print(d)
# # d['k1'] = 'new'
# # print(d)
# # print(d.keys())
# # print(d.values())
# # print(d.items())
# #
# # Tuples
# # tup = (1,2,3)
# # my_list =[1,2,3]
# # print(len(tup))
# # print(tup[0])
# # t = ('a','a','b')
# # print(t.count('a'))
# # my_list[0] = '1000'
# # print(my_list)
# #
# # Set - Множество
# # my_set = set()
# # my_set.add(1)
# # print(my_set)
# # my_set.add(2)
# # print(my_set)
# # my_list = [1, 1, 2, 3, 4, 5, 6, 4, 4, ]
# # print(set(my_list))
# #
# # Boolean
# # print(type(True))
# #
# # # Работа с файлами
# # # myfile = open('myfile.txt')
# # # myfile.read()
# # myfile = open('/home/evgeny/PycharmProjects/200425/myfile.txt')
# # # myfile.close()
# #
# # Statement - операторы if,else
# # hungry = True
# # if hungry:
# #     print('Im hungry')
# # else:
# #     print('Im not hungry')
# #
# # loc = 'Store'
# # if loc == 'Auto shop':
# #     print('Cars are cool')
# # elif loc == 'Bank':
# #     print('Money')
# # elif loc == 'Store':
# #     print('Магаз')
# # else:
# #     print('I dont know')
# #
# # loop - for-----------------------------
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in mylist:
#     print('hello')
#
# for i in mylist:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print(f'Odd number: {i}')
#
# list_sum = 0
# for i in mylist:
#     list_sum = list_sum + i
#     print(list_sum)
# print(list_sum)
#
# mystring = 'hello world'
# for letter in mystring:
#     print(letter)
#
# tup = (1,2,3)
# for i in tup:
#     print(i)
# mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
# for a, b in mylist:
#     print(a)
#     print(b)
#
# d = {'k1': 1, 'k2': 2, 'k3': 3}
# for item in d.items():
#     print(item)
# #
# # while________________________
# # x = 0
# # while x < 5:
# #     print(f'Текущее значени x равно {x}')
# #     x += 1
# # else:
# #     print('x больше или равен 5')
# #
# # x = [1,2,3]
# # for i in x:
# #     pass
# #
# # x = 'Sammy'
# # for i in x:
# #     if i == 'a':
# #         continue
# #     print(i)
# #
# # x = 'Sammy'
# # for i in x:
# #     if i == 'a':
# #         break
# #     print(i)
# #
# # Полезные операторы________________________________
# # mylist = [1,2,3]
# # for i in range(3, 10,2):
# #     print(i)
# # a =list(range(10))
# # print(a)
# #
# # index_count = 0
# # word = 'abcde'
# # for item in enumerate(word):
# #     print(item)
#
# # mylist1 = [1, 2, 3, 4]
# # mylist2 = ['a', 'b', 'c']
# # for item in zip(mylist1, mylist2):
# #     print(item)
#
# # mylist = [10, 20, 30, 40]
# # print(min(mylist))
# #
# # from random import shuffle
# #
# # mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(shuffle(mylist))
# #
# # from random import randint
# # a = randint(0,100)
# # print(a)
#
# List comprehension -Генератор списков_________________________
mylist = [letter for letter in "fja;afds"]
print(mylist)

mylist = [x**2 for x in range(0, 11) if x%2 ==0]
print(mylist)

# celsium = [0, 10, 20, 34.5]
# # fahrenheit =[((9/5)*temp +32) for temp in celsium]
# # print(fahrenheit)
#
# fahrenheit =[]
# for temp in celsium:
#     fahrenheit.append(((9 / 5) * temp + 32))
# print(fahrenheit)
