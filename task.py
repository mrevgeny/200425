# Используйте for, .split() и if, чтобы написать команду,
# которая выведет только те слова, оторые начинаются с буквы 's':
# st = 'String Print only the words that start with s in this sentence'
# for item in st.split():
#     if item[0].lower() == 's':
#         print(item)

# for i in range(1,51):
#     if i % 3 == 0:
#         print(i)

# text= 'Love thy neighbor'
# # разделяем строку
# print(text.split())
# grocery = 'Milk, Chicken, Bread'
# # разделяем запятой
# print(grocery.split(', '))
# # разделяем двоеточием
# print(grocery.split(':'))
# a =[x for x in range(1,51) if x%3 == 0]
# print(a)

# st = 'String Print only the words that start with s in this sentence'
# for word in st.split():
#     if len(word)%2 == 0:
#         print(word)

# for num in range(1,101):
#     if num%3 == 0 and num%5 == 0:
#         print('FizzBuzz')
#     elif num%3 ==0:
#         print('Fizz')
#     elif num%5==0:
#         print('Buzz')
#     else:
#         print(num)
# st = 'String Print only the words that start with s in this sentence'
# a = [word[0] for word in st.split()]
# print(a)

# def lesser_of_two(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a < b:
#             result = a
#         else:
#             result = b
#     else:
#         if a > b:
#             result = a
#         else:
#             result = b
#     return result
#
#
# print(lesser_of_two(12, 7))
#
# def make_twenty(n1, n2):
#     if n1 + n2 == 20:
#         return True
#     elif n1 == 20:
#         return True
#     elif n2 == 20:
#         return True
#     else:
#         return False
#
#
# print(make_twenty(20, 5))

# def old_macdon(name):
#     first_letter = name[0]
#     inbetween = name[1:3]
#     fourth_letter = name[3]
#     rest = name[4:]
#     return first_letter.upper() + inbetween + fourth_letter.upper() + rest
#
# print(old_macdon('macdonalds'))

# def blackjack(a, b, c):
#     if sum([a, b, c]) <= 21:
#         return sum([a, b, c])
#     elif 11 in [a, b, c] and sum([a, b, c]) - 10 <= 21:
#         return sum([a, b, c]) - 10
#     else:
#         return 'Bust'
#
#
# print(blackjack(8, 8, 11))

#lambda
# def square(num):
#     result = num ** 2
#     return result
# print(square(3))
#
# square =lambda  num: num **2
# print(square(4))
