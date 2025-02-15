#1 Oski Stole Your Power
#Oski hacked your computer and you can no longer use x**y or pow(x, y). Find a different
#way (by writing a function) that can compute x raised to the power of y.

def computepower(x, y):
    answer = 1
    for i in range(0, y):
        answer*=x
    return answer
computepower(2,10)
#2 What Should I Wear?
#You are trying to decide what to wear to the Python DeCal lecture, but you
#are only concerned about the day’s lowest and highest temperatures. Write a
#function that takes in a list as input and returns a tuple with the min and max as two values.

readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(values):
    minmaxlist= []
    minmaxlist.append(min(values))
    minmaxlist.append(max(values))
    return minmaxlist
temperatureRange(readings)
#3 Check if its the Weekend
#All your classes have assigned problem sets due next week, and you want to
#check if it’s the weekend so you have time to work on them. Write a function
#that takes a day of the week (represented as an integer, where 1 = Monday, 2
#= Tuesday, etc) and returns True if its a weekend and False if otherwise.
today = 6 # Saturday
def isWeekend(day):
    if 1<= day <=5:
        return False
    elif 6<= day <=7:
        return True
    else:
        return ('Not A Day')
isWeekend(today)
#4 Fuel Efficiency Calculator
#The Python DeCal wants to take a trip to the Lick Observatory ( San Jose,
#CA) and they want to pick the best car. Write a function that takes the distance
#traveled (in miles) and the amount of fuel consumed (in gallons) as input and
#returns the fuel efficiency.
distance = 70 # miles
fuel = 21.5 # gallons
def fuel_efficiency(distance, fuel):
    return distance/fuel
fuel_efficiency(70, 21.5)
#5 Secret Code
#Write a function that takes an integer as input and moves its last digit to the
#front of the number. You may NOT convert the input to a string. Hint: Try
#modulus (%) and floor division (\\) to solve this problem.
n = 12345
def decodeNumbers(n):
    j = 0
    while n>0:
        n//10 == n
        j+=1
        print(j)
    #part1 = (n//10)*10
    #part2 = n%part1
    #return part2*10**4 + part1/10
decodeNumbers(n)
j = 0
while n>0:
    n//10 == n
    j+=1
    print(j)
'''6 Min & Max but with Loops!
Oh no! Oski hacked you computer again... now you have lost the ability to use
min() and max().
6.1 For Loops
Write two functions to manually find the minimum and maximum values in a
list of numbers with for loops.
>>> nums = [2024, 98, 131, 2, 3, 72]
>>> find_min_with_for_loop(nums)
2
>>> find_max_with_for_loops(nums)
2024
6.2 While Loops
Write two functions to manually find the minimum and maximum values in a
list of numbers with while loops.
>>> nums = [2024, 98, 131, 2, 3, 72]
>>> find_min_with_while_loop(nums)
2
2
>>> find_max_with_while_loops(nums)
2024
7 Counting Vowels
Write a function that takes a string as an input and returns the number of vowels
in the string and the number of consonants in the string as tuple. Don’t forget
about capital letters! Hint: You can use .isalpha() to check if a character is
a letter.
>>> text = "UC Berkeley, founded in 1868!"
>>> vowel_and_consonant_count(text)
(4, 11)
8 Calculate Digital Root
Write a function that takes an integer as an input and returns the sum of its
digits.
>>> num = 2468
>>> digital_root(num)
20
'''
