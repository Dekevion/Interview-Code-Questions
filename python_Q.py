# The goal of this is to improve upon my critical thinking skills. Start small


def stringy_string(str, n):
    result = ""
    for i in range(n):
        result = result + str
    print(result)


stringy_string('Hello', 2)

letters = ['A', 'B', 'C']
# [print(each_element) for each_element in letters]

for i in range(len(letters)):
    print('Letter {}: {}'.format(i + 1, letters[i]))


# def front_times(str, n):
#     front_len = 3
#     if front_len > len(str):
#         front_len = len(str)
#     front = str[:front_len]
#
#     result = ""
#     for i in range(n):
#         result = result + front
#     return result

def every_other_string(str):
    # initialize result variable so that i can do something with it
    result = ""
    # for each_element in the range of the length of the string
    # each_element modulo 2 means every other string (even number)
    for each_element in range(len(str)):
        if each_element % 2 == 0:
            result = result + str[each_element]
        print(result)


#
# every_other_string("Dekevion")
#


#
# def string_explosion(str):
#     result = ""
#     for each_element in range(len(str)):
#         result = result + str[:each_element + 1]
#     print(result)
#
#
# string_explosion('code')
#


# def front_times(str, n):
#     front = 3
#     if front > len(str):
#         front = len(str)
#     front = str[:front]
#     result = ""
#     for i in range(n):
#         result = result + front
#     print(result)


# front_times('Chocolate', 2)
#


#
# def make_tags(tag, word):
#     print(f"<{tag}>{word}<{tag}>")
#
#
# make_tags("i", "me")
#
# list = [1, 2, 3, 4]
#
# if len(list) > 1 and list[0] == list[-1]:
#     print(True)
# else:
#     print(False)


# def solution(A):
#     n = len(A)
#     result = 0
#     for i in range(n - 1):
#         if (A[i] == A[i + 1]):
#             result = result + 1
#     r = 0
#     for i in range(n):
#         count = 0
#         if (i > 0):
#             if (A[i - 1] != A[i]):
#                 count = count + 1
#             else:
#                 count = count - 1
#         if (i < n - 1):
#             if (A[i + 1] != A[i]):
#                 count = count + 1
#             else:
#                 count = count - 1
#         r = max(r, count)
#     print (result + r)
# solution([0,0,0,1,0,0])


# Question 1)
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on
# vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# Question 2)

# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

# The question asks to print True if both monkeys equal each other.

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile == True:
        print(False)
    elif a_smile and b_smile == False:
        print(False)


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.


def two_ints(a, b):
    if int(a) == int(b):
        print((a + b) * 2)
    else:
        print(a + b)


# two_ints(2, 1)


# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# def fizzBuzz(n):
#     print(n)
#     if(n % 3 == 0 and n % 5 == 0):
#         print("FizzBuzz")
#     elif (n % 3 == 0 and n % 5 != 0):
#         print("Fizz")
#     elif (n % 5 == 0 and n % 3 != 0 ):
#         print("Buzz")
#     elif (n % 3 != 0 or n % 5 != 0):
#         print(n)
#
# fizzBuzz(3)


myPlayList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

myNumberPlayList = [1, 2, 3]

for each_el in myNumberPlayList:
    result = 0
    each_el += result
    print(result)

for x in myPlayList:
    print(x)

for each_element in range(len(myPlayList)):
    print('Letter {}: {}'.format(each_element + 1, myPlayList[i]))

aliceArray = [1, 2, 3]

bobArray = [2, 1, 4]
numArray = [1, 1]


def compareTriplets(a, b):
    alicesNum = 0
    bobsNum = 0

    if a[0] > b[0]:
        alicesNum += 1
    elif b[0] > a[0]:
        bobsNum += 1
    elif a[1] > b[1]:
        alicesNum += 1
    elif b[1] > a[1]:
        bobsNum += 1
    # elif a[2] > b[2]:
    #     alicesNum += 1
    # elif b[2] > a[2]:
    #     bobsNum += 1
    print([alicesNum, bobsNum])


arrayA = [5, 6, 7]
arrayB = [6, 7, 10]
compareTriplets(arrayA, arrayB)