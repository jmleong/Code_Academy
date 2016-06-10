################################
##----------CODE ACADEMY--------
##----------Python Examples-----
################################

#########################################
#------ Lesson: A Day At the Supermarket
#########################################

#########
#~~~3/13: Control Flow and Looping
#######################################
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
even_list = []
#i = 0
for even in a:
    if even % 2 == 0:
        # "Even number in a is: %i" %even
        # "Len of list %i" %len(even_list)
        # CANNONT DO: even_list[i] = even
        # CANNOT DO: i = i + 1
        # even_list.append(even) //*If you want to save all the evens in a list
        print even
#print even_list //*If you want to save all the evens in a list

#########
#~~~4/13: Lists + Functions
#######################################
My Task)
Write a function that counts how many times the string "fizz" appears in a list.

Write a function called fizz_count that takes a list x as input.
Create a variable count to hold the ongoing count. Initialize it to zero.
for each item in x:, if that item is equal to the string "fizz" then increment the count variable.
After the loop, please return the count variable.
For example, fizz_count(["fizz","cat","fizz"]) should return 2.
---------------------------------------------------------------------------
# Write your function below!
def fizz_count(x):
    count = 0 #Initialize count to zero
    for item in x:
        if item == "fizz":
            count = count + 1
    return count

print fizz_count(["fizz","cat","fizz"])
# Returned 2

#########
#~~~9/13: Shopping at the Market
#######################################
# Dictionary of Prices
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Dictionary of Stock
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

## Since both dictionaries have the same keys, we can loop through
## one dictionary and show values from both of them.
# Loop through each key and list the price and stock amount

for key in prices.keys():
    print key #key name
    print "price: %s" % prices[key] #price
    print "stock: %s" % stock[key] #stock

#Total Value of inventory
total = 0
for key in prices:
    total = total + (prices[key] * stock[key])

print total

############################################
#------ Lesson: Student Becomes the Teacher
############################################
 
#########
#~~~6/9: How to continue on the next line
####################################### 
cost = {
    "apples": [3.5, 2.4, 2.3],
    "bananas": [1.2, 1.8],
}

return 0.9 * average(cost["apples"]) + \
0.1 * average(cost["bananas"])

The \ character is a continuation character. 
The following line is considered a continuation of the current line.

#########
#~~~9/9: Student Becomes the Teacher
####################################### 
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# Add your function below!
def average(lst):
    size = len(lst)
    total = 0
    for score in lst:
        total = total + score
    return float(total)/size

# Get_average function
def get_average(student):
    homework = average(student["homework"])
    quiz = average(student["quizzes"])
    tests = average(student["tests"])
    return homework * 0.1 + quiz * 0.3 + tests * 0.6

# Get_letter_grade; score is a number
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else: 
        return "F"

# Get_class_average; students is a list containing the 3
# students
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

#test
class_lst = [lloyd, alice, tyler]

#for student in class_lst:
#    print get_average(student)

# Print Class average
print get_class_average(class_lst)
# Print Class Letter grade
print get_letter_grade(get_class_average(class_lst))

############################################
#------ Lesson: Lists and Functions
############################################
 
#########
#~~~10/18: Modifying an element of a list in a function
#########################################################
def list_function(x):
    #Add 3 to the item at index 1 and store result in index 1
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print list_function(n)
#[3, 8, 7]

#########
#~~~12/18: Printing out a list item by item in a function
##########################################################
n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print x[i]

print print_list(n)

#########
#~~~14/18: Passing a range into a function
##########################################################
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) 
#[0, 2, 4]

#########
#~~~15/18: Iterating over a List in a function
###############################################
n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result

print total(n)
#15

#########
#~~~17/18: Using two lists as two arguments in a function
##########################################################
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
    return x + y

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

#########
#~~~18/18: Using a list of lists in a function
###############################################
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for items in numbers:
            results.append(items)
    return results

print flatten(n)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

###################################################
#------ Lesson: Battleship
###################################################

#########
#---Making a 5x5 Grid using lists
###############################################
board = []

# Create a 5x5 grid of Os
for lst in range(5):
    board.append(["O"] * 5)

# Function to print board in a Grid
def print_board(board):
    for row in range(5):
        print board[row]

print_board(board)
#['O', 'O', 'O', 'O', 'O']
#['O', 'O', 'O', 'O', 'O']
#['O', 'O', 'O', 'O', 'O']
#['O', 'O', 'O', 'O', 'O']
#['O', 'O', 'O', 'O', 'O']

#Because print ['O'] * 5 
#= ['O', 'O', 'O', 'O', 'O']

############################################
#------ Lesson: Practice Makes Perfect
############################################

#########
#---is_int (3/15)
###############################################
#  Find integers: 7.0 is an int
#    Hint: If the difference between a number and that same number rounded down is 
#      greater than zero, what does that say about that particular number?
def is_int(x):
    if round(x) == x:
        return True
    else:
        return False

print is_int(7.0)   # True
print is_int(7.5)   # False
print is_int(-1)    # True
print is_int(5.1)   # False

#########
#---reverse (7/15)
###############################################
#  Define a function called reverse that takes a string textand returns that string in reverse.
#  For example: reverse("abcd") should return "dcba".
#  You may not use reversed or [::-1] to help you with this.
#  You may get a string containing special characters (for example, !, @, or #).

def reverse(text):
    if len(text) <= 1:
        return text
        
    return reverse(text[1:]) + text[0]
    
print reverse('hello')

#########
#---anti_vowel (8/15)
###############################################
#  Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
#    For example: anti_vowel("Hey You!") should return "Hy Y!".
#    Don't count Y as a vowel.
#    Make sure to remove lowercase and uppercase vowels.

def anti_vowel(text):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for i in text:
        if i in vowel:
            text = text.replace(i,"")
    return text

print anti_vowel("How are you?")

#########
#---scrabble_score (9/15)
###############################################
#  Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
#    Assume your input is only one word containing no spaces or punctuation.
#    As mentioned, no need to worry about score multipliers!
#    Your function should work even if the letters you get are uppercase, lowercase, or a mix.
#    Assume that you're only given non-empty strings.
#    Hint: Have your function loop through the word that you are given as input and look up the score for each letter in the score dictionary. 
#      Add the score for each letter into a total of some sort.
#      Remember you can use the string.lower() method to make your string lower case!

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for i in word.lower():
        if i in score:
            total = total + score[i]
    return total

print scrabble_score('Helix')

#########
#---censor (10/15)
###############################################
#  Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.
#    For example:
#      censor("this hack is wack hack", "hack") 
#    should return
#      "this **** is wack ****"
#  Assume your input strings won't contain punctuation or upper case letters.
#  The number of asterisks you put should correspond to the number of letters in the censored word.
#    Hint: You can use
#      string.split()
#      # and 
#      " ".join(list)
#    to help you here.
#    Remember:
#      "*" * 4 equals "****"
#    After splitting the string with string.split(), you can loop through the indices in 
#    the list and replace the words you are looking for with their asterisk equivalent. 
#    Join the list at the end to get your sentence!

#My Code 
def censor(text, word):
    text = text.split(" ")
    count = 0
    for i in text:
        if i == word:
            text[count] = "*"*len(word)
        count += 1
   return " ".join(text)

print censor("this hack is wack hack", "hack")

#1. one line code:
def censor(text, word):
    return text.replace(word, ("*"*len(word)))
print censor("this hack is wack hack", "hack")

#2. one line code:
def censor(text, word):
    return ' '.join([('*' * len(word)) if x == word else x for x in text.split()])
 
#########
#---count (11/15)
###############################################
#  Define a function called count that has two arguments called sequence and item.
#  Return the number of times the item occurs in the list.
#  For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
#    There is a list method in Python that you can use for this, but you should do it the long way for practice.
#    Your function should return an integer.
#    The item you input may be an integer, string, float, or even another list!
#    Be careful not to use list as a variable name in your code—it's a reserved word in Python!

#My Code 
def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total += 1
    return total
print  count(["g",2,"g",1,2,1,1],"g") #2

#1. one line code
def count(sequence, item):
    return sum(item==numbers for numbers in sequence)

#########
#---purify (12/15)
###############################################
#  Define a function called purify that takes in a list of numbers, removes all odd numbers in the list,
#  and returns the result.
#  For example, purify([1,2,3]) should return [2].
#  Do not directly modify the list you are given as input; instead, return a new list with only the even
#  numbers.

#My Code
def purify(numbers):
    purify_list = []
    for i in numbers:
        if i % 2 == 0:
            purify_list.append(i)
    return purify_list

print purify([1,2,3,4])

#1. one line code:
def purify(sequence):
  return [i for i in sequence if i % 2 == 0]
 
#########
#---product (13/15)
###############################################
#  Define a function called product that takes a list of integers as input and returns the product of all of
#  the elements in the list.
#  For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
#  Don't worry about the list being empty.
#  Your function should return an integer.

#My Code
def product(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

print product([4, 5, 5])

#1. one line code
product = lambda lst: reduce(lambda x,y:x*y,lst)
print product([4, 5, 5])

#########
#---remove_duplicates(14/15)
###############################################
#  Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
#  For example: remove_duplicates([1,1,2,2]) should return [1,2].
#  1. Don't remove every occurrence, since you need to keep a single occurrence of a number.
#  2. The order in which you present your output does not matter. So returning [1,2,3] is the same as returning [3,1,2].
#  3. Do not modify the list you take as input! Instead, return a new list.
#    Hint: The easiest way to approach this problem is to create a new list in your function, loop through your input list, 
#    and add items from your input list to your new list if the current item is not already contained in your new list. 
#    Using the "a not in b" syntax might help you here.
#        "a not in b" syntax
#    Also, note that destructively modifying a list while you are looping through it is bad practice and will likely lead to
#    bugs somewhere down the line! That's why we always make a fresh copy to work on.

# My Code
def remove_duplicates(numbers):
    newlst = []
    for number in numbers:
        if number not in newlst:
            newlst.append(number)
    return newlst

print remove_duplicates([1,1,2,2,3,4,4])

############################################
#Lesson 10: Introduction to BIT Wise operators
############################################

#########
#---The Man Behind the Bit Mask (11/14)
########################################################
# A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.
#
#    num  = 0b1100
#    mask = 0b0100
#    desired = num & mask
#    if desired > 0:
#            print "Bit was on"
#
# In the example above, we want to see if the third bit from the right is on.
#
# First, we first create a variable num containing the number 12, or 0b1100.
# Next, we create a mask with the third bit on.
# Then, we use a bitwise-and operation to see if the third bit from the right of num is on.
# If desired is greater than zero, then the third bit of num must have been one.
#
#Problem:
# 1. Define a function, check_bit4, with one argument, input, an integer.
# 2. It should check to see if the fourth bit from the right is on.
# 3. If the bit is on, return "on" (not print!)
# 4. If the bit is off, return "off".

# My Code
def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"