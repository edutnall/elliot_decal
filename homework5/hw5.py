#1 HW1/HW2 Review: The Terminal + Com-mand Line + Git
#In your .py file, please answer these questions as comments. Pretend your name is Judy.
#1. You have been plopped into this directory system. What command will
#tell you what your working directory is?
# The command 'pwd'.
#2. The command tells you ∼/python decal/judy decal. What command
#will list all the files in your current working directory?
# The command 'ls'.
#3. Brianna just sent out an announcement that there was a typo on homework.py. So you need to pull the updates. 
# What commands will let you move to the correct repository and pull the latest changes?
#The following commands:
# cd ~/python_decal/judy_decal/
# git pull origin main
#4. How would you move this new homework.py to your personal repository homework directory?
# mv homework.py ~/python_decal/judy_decal/homework/
#5. You want to see the contents of the homework.py in your terminal from
#your personal repository. What command(s) will let you do this?
# nano homework.py
#6. You want to edit the contents of the homework.py in your terminal from
#your personal repository. What command will let you do this?
# nano homework.py
#7. You have finished the homework. What commands will allow you to save
#the changes and push from your local repository to your remote repository?
# git add .
# git commit -m "finished homework"
# git push origin main
#8. Oh no! Git gave you the following error. What commands should you call
#to resolve this error and push your homework properly? What does the
#error mean? (i.e. what did ”Judy” do wrong?)
'''! [rejected] main -> main (fetch first)
error: failed to push some refs to ’https://github.com
/judy/judy_decal.git’
hint: Updates were rejected because the remote contains
work that you do
hint: not have locally. This is usually caused by another
repository pushing
hint: to the same ref. You may want to first integrate
the remote changes
hint: (e.g., ’git pull ...’) before pushing again.
hint: See the ’Note about fast-forwards’ in ’git push
--help’ for details.'''
# git pull origin main
# git push origin main
#9. What absolute path will allow you to move to Recents/?
# cd ~/Recent/
#HW3 Review: Data Types + Functions + Conditionals + Loops
#2.1 Data Types
#Write a function that takes any input and returns a string indicating its data type.
def checkDataType(input):
    print(type(input))
checkDataType(3.14)
checkDataType(True)
#2.2 Conditionals
#Write a function that takes an integer as input and returns ’Even’ if the integer
#is even, and ’Odd’ otherwise.
def evenOrOdd(input):
    if input%2 == 0:
        return 'Even'
    else:
        return 'Odd' 
evenOrOdd(7)
evenOrOdd(10)
#3 Loops
#Write a function that takes a list of integers and returns their sum using a loop
#(do NOT use the built-in sum() function).
numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    sum = 0
    for i in range(0, len(numbers)+1):
        sum += i
    return sum
sumWithLoop(numbers)
#4 HW4 Review: Lists
#4.1 Lists
#Write a function that takes a list and returns a new list with each element duplicated.
list = ['a', 'b', 'c']
def duplicateList(list):
    newlist = []
    for i in range(0, len(list)):
        newlist.append(list[i])
        newlist.append(list[i])
    return newlist
duplicateList(list)
#4.2 Debugging
#There’s an error in the following function that’s supposed to return the square
#of a number. Find and correct it:
def square(num):
    return num * num
square(53)
# The error is a SyntaxError caused by the function definition line not having a ':' after it.
#5 HW2 Review: Git
#Please take a screenshot of you adding, committing and pushing this home-
#work from your local to your remote repository. Include this screenshot in your
#Gradescope submission!
