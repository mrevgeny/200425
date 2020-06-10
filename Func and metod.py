# Методы
# mylist = [1, 2, 3]
# mylist.append(4)
# print(mylist)

# # Функции______________________________
# def func(x,y):
#     print(x+y)
# func(2,9)
#
# def say_hallo(name='Имя'):
#     print('Привет '+name)
# say_hallo()
# # returt позволяет вернуть результат работы и его можно сохранить в переменную
# def add(n1,n2):
#     return n1+n2
# result=add(10,20)
# print(result)
#
# def cat_check(mystr):
#     if 'Кот' in mystr:
#         return True
#     else:
#         return False
# print(cat_check('Кот'))
# #поросячья латынь
# def pig_latin(word):
#     first_letter = word[0]
#     if first_letter in 'aeiou':
#         pig_word = word +'ay'
#     else:
#         pig_word  = word[1:]+ first_letter +'ay'
#         return pig_word
# print(pig_latin('word'))
# *args **kwargs___________________________________
# def myfunc(a, b, c=0):
#     return sum((a, b)) * 0.05
#
#
# print(myfunc(40, 60))

# args передает любое нужное количество параметров
# def myfunc(*args):
#     return sum(args) * 0.05
#
#
# print(myfunc(11, 3, 4, 5, 5))

# передает ключ в словаре
# def myfunc(**kwargs):
#     if 'fruit' in kwargs:
#         print('My fruit is {}'.format(kwargs['fruit']))
#     else:
#         print('No fruit here')
#
#
# myfunc(fruit='apple')


def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like{} {}'.format(args[2], kwargs['food']))


myfunc(10, 20, 30, fruit='orange', food='eggs')

