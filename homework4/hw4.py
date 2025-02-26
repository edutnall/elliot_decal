#1 Debugging
#As you work through this problem set, whenever you encounter an error, please
#include a comment explaining what the error was and how you later resolved it.
#You can add these explanations at any relevant place in the file. Example:
#>>> print("Hello, World!")
"""
>>> I encountered the following eror: "SyntaxError: unterminated
>>> string literal (detected at line 1) when I wrote
>>> print("Hello, World!)". So I added the missing " at the end
>>> and the code printed it successfully.
>>> """
#2 Practicing Sliding & Striding
#In this problem, you will practice slicing and striding lists!
#2.1 Making a List Variable
#Create a variable (name it anything you want, but make it descriptive!) that
#is assigned to a list with numbers 0 through 20. You should not write each
#number manually.

numberlist = []
for i in range(0, 21): #I set the range as (0, 20), so it only printed 0 through 19
    #and adding 1 to the range fixed the problem.
    numberlist.append(i)
print(numberlist)


#2.2 Working with List Elements
#Write a function that will take in your list from Part 2.1 and square each element
#in the list. Assign the result to a new variable.

def squareList(list):
    squarednumbers= []
    for i in range(0, 21):
        squarednumbers.append((list[i])**2)
    return squarednumbers #I put a print statement here, because of which the variable
    #type in the next part was a 'None' instead of list. By turning this into a return
    #statement, the function always returns a list and can be put into other functions.
squareList(numberlist)

#2.3 Slicing
#Write a function that takes in your new list from Part 2.2 and returns the first
#15 elements of the list using slicing.
squarelist = squareList(numberlist)
def first_fifteen_elements(list):
    fifteenlist = []
    fifteenlist.append(list[0:15])
    return fifteenlist
first_fifteen_elements(squarelist)
[0, 1, 4, ..., 196]
#2.4 Striding
#Write a function that takes in your list from Part 2.2 and returns every 5th
#element from the list using striding.
squarelist = squareList(numberlist)
def every_fifth_element(list):
    fifthlist = []
    fifthlist.append(list[4:21:5]) #First number is 4 because I realized
    #that I needed to start on the n-1 index to accurately return the 5th element.
    return fifthlist
every_fifth_element(squarelist)
[16, 81, 196, 361]
#2.5 Slicing & Striding
#Write a function that takes your list from Part 2.2, slices the last 3 elements of
#the list, and then returns every 3rd element from that list in reverse order.
squarelist = squareList(numberlist)
def fancy_function(input):
    list1 = input[::-1] 
    list2 = list1[0:-2] #[0:-3] returned every correct value except for the last one.
    #Modfifying this to [0:-2] fixed it and returned the correct value.
    list3 = []
    list3.append(list2[0:20:3])
    return list3
fancy_function(squarelist) 
[400, 289, 196, 121, 64, 25, 4]
#3 2D lists
#3.1 Creating a 5x5 2D List
#Write a function that uses nested for loops to create a 5x5 2D list where the
#numbers 1 through 25 are stored sequentially. Assign the result to a new vari-
#able.
def create_2d_list(x, y):
    matrix=[]
    for i in range(0, y):
        matrix.append([])
    a = 1 
    for j in range(0, y): #I originally had this as x*y, which returned the error of index out of range.
        #Instead had my numbers be assigned by the value a instead of by a for loop, which allowed me to fix
        #the indices and get rid of the error to create a matrix.
        for k in range(0,x):
            matrix[j].append(a)
            a += 1
    return matrix
create_2d_list(5,5)
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
#3.2 Replacing 2D List with Multiples of 3
#With the 2D list you created in Part 3.1, write a function that will replace all
#multiples of 3 with the character “?”.
matrix = create_2d_list(5,5)
def modified_2d_list(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j]%3 ==0:
                matrix[i][j] = '?'
    return matrix
modified_2d_list(matrix)
'''[[1, 2, ‘?’, 4, 5],
[‘?’, 7, 8, ‘?’, 10],
[11, ‘?’, 13, 14, ‘?’],
[16, 17, ‘?’, 19, 20],
[‘?’, 22, 23, ‘?’, 25]]'''
#3.3 Summing None-’ ?’ Elements
#Assign the result of your function from Part 3.2 to a variable. Write a function
#that will iterate through the new 2D list variable and return the sum of all the
#elements that are not “?”. Hint: Try using “!=”.
matrix = create_2d_list(5,5)
modmatrix = modified_2d_list(matrix)
def sum_non_question_elements(modmatrix):
    sum = 0
    for i in range(0,len(modmatrix)):
        for j in range(0, len(modmatrix[0])):
            if modmatrix[i][j] != '?':
                sum += modmatrix[i][j]
    return sum
sum_non_question_elements(modmatrix)
217
