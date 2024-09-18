#TODO Write a Python program to find the sum of all even numbers from 1 to 100 using a loop.
from numpy.version import short_version


def sum_even_numbers():
    """"Calsulates sum of all numbers from 1 to 100 and returns total"""
    total=0
    for num in range(1,101):
        if num%2==0:
            total+=num
    return total
# print(sum_even_numbers())

#TODO Create a program that checks if a given number is prime or not using a loop and conditional statements.
def is_prime(n):
    """Takes a numbers as input and returns True if it is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# print(is_prime(1122))

#TODO Write a function that takes a list of numbers and returns a new list with only the even numbers.
def even_list(inputlist):
    """Takes a list of numbers as input and returns a list with all even numbers"""
    even = []
    for items in inputlist:
        if items % 2 == 0:
            even.append(items)
    return even
# print(even_list([1,2,3,4,5,6,7,8,9]))


#TODO Create a dictionary representing a student's grades in different subjects. Calculate the average grade.

# Dictionary representing a student's grades
student_grades = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "History": 88,
    "Art": 95
}



def calculate_avg_grade(studentdict):
    """Takes a dict of student gradws as input and returns calsulated avg grade"""
    added_grades=0
    for key in studentdict:
         added_grades+= studentdict[key]
    avg_grade=added_grades/len(studentdict)
    return avg_grade

# print( "calculate_avg_grade(student_grades)")




#TODO Write a program that reverses a given string without using any built-in reverse function.
def reverses_string():
    user_input= input("Enter a string to reverse ")
    size= len(user_input)-1
    reversed=""
    while size>=0:
        reversed+=user_input[size]
        size-=1
    print(f"your string reversed is  {reversed}")

# reverses_string()
#TODO Create a function that finds the factorial of a given number using a loop.
def find_factorial(number):
    factorial=1
    for num in range(1,number+1):
        factorial*=num
    return factorial

# print(find_factorial(4))
#TODO Write a Python program that counts the number of vowels in a string.
def count_vowels():
    count=0
    word= input("Enter a string ").lower()

    for char in word:
        if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" :
            count+=1
    print(count)

# count_vowels()

#TODO Given a list of names, write a program to find the shortest and longest names in the list.
def find_short_long():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    shortest=names[0]
    longest = shortest
    for name in names:
        if len(name)>len(longest):
            longest=name
        elif len(name)<len(shortest):
            shortest=name

    print(f"Shortest name : {shortest} \n longest name : {longest}")
# find_short_long()
#TODO Implement a function that checks if a given word is a palindrome.
def palindrome():
    word= input("Enter a word ").lower()
    size=len(word)
    ispalin= True
    i=size-1
    for char in range(int(size/2)):
        if word[char]== word[i]:
            i-=1
            ispalin=True
        else:
            ispalin =False
            break
    print(ispalin)

# palindrome()


#TODO Write a program that generates a list of Fibonacci numbers up to a specified limit.
def fibonacci(limit):
    first=0
    second=1
    new=0
    sequance=[]
    sequance.append(first)
    sequance.append(second)

    while new <limit:
        sequance.append(new)
        new= first + second
        first=second
        second=new
    print(sequance)
# fibonacci(2000)
#TODO Create a program that finds the intersection of two lists.
def intersection():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common=[]
    for i in list1:
        for j in list2:
            if i==j:
                common.append(j)
    print(common)
# intersection()

#TODO Write a Python script that replaces all occurrences of a specific word in a text with another word.
def replaces():
    text="My name is abdul Hannan"
    replacewith="b"
    character_to_replace="a"
    text= text.replace(character_to_replace,replacewith)
    print(text)
# replaces()
#TODO Implement a function that finds the maximum and minimum values in a tuple of numbers.
def minmax_tuple_of_num():
    # Tuple of numbers
    numbers = (10, 20, 30, 40, 50)
    min=numbers[0]
    max=min
    for num in range (len(numbers)):
        if numbers[num]>max:
            max=numbers[num]
        elif numbers[num]<max:
            min=numbers[num]
    # Print the tuple
    print(min , max)

# minmax_tuple_of_num()
#TODO Create a program that sorts a list of strings in alphabetical order.
def sort_list():
    # Larger unsorted list of strings
    cities = [
        "Tokyo", "New York", "London", "Paris", "Berlin", "Sydney", "Toronto",
        "Mumbai", "Beijing", "Moscow", "Dubai", "Rome", "Istanbul", "Bangkok",
        "Los Angeles", "Chicago", "Hong Kong", "Singapore", "Madrid", "Vienna"
    ]

    # Print the list
    cities.sort()
    print(cities)
# sort_list()
#TODO Write a Python function that accepts a list of integers and returns a new list with unique values (no duplicates).

def unique():
    test_list = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 10, 3, 4]
    print("The original list is : "
          + str(test_list))

    # using set() to remove duplicated from list
    test_list = list(set(test_list))

    # printing list after removal
    # distorted ordering
    print("The list after removing duplicates : "
          + str(test_list))


# unique()






