import numpy as np
#1 Prime Clusters
#You have obtained a dataset of star temperatures from different stellar clusters.
#For your research, you are interested only in clusters where at least one star’s
#temperature is a prime number. Given a 2D NumPy array, write a function to
#find the rows where at least one value is a prime number. For example:
arr = np.array(([2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]))
def containsPrimes(arr):
    def isprime(n):
        for d in range(2, n):
            if n % d == 0:
                return False
        return True
    result = 0
    for i in range(0, len(arr)):
        for j in arr[i]:
            if isprime(j):
                if type(result) == int:
                    result = [arr[i]]
                    break
                result = np.concatenate((result, [arr[i]]), axis =0)
                break
    return result
containsPrimes(arr)
#2 Let’s play Checkers!
#You’ve decided to take a break from your cutting-edge research and play checkers
#with your friend. Unfortunately, there is no checkerboard in sight! Therefore
#you must create one yourself.
#2.1
#Start by writing a function that creates a 8x8 square matrix with only zeros.
def checkerboard(size):
    array = np.zeros((size, size), np.int8)
    return array
checkerboard(8)
#2.2
#For only the odd rows, make an alternating pattern of ones and zeroes.
checkers = checkerboard(8)
def altodds(checkers):
    for i in range(0, len(checkers)):
        for j in range(0, len(checkers[0])):
            if (i+j)%2 ==0 and i%2 ==0:
                checkers[i][j] = 1
    return checkers
altodds(checkers)
#2.3
#Finish the checkerboard with the even rows.
checkers = checkerboard(8)
def altboth(checkers):
    for i in range(0, len(checkers)):
        for j in range(0, len(checkers[0])):
            if (i+j)%2 ==0:
                checkers[i][j] =1
    return checkers
altboth(checkers)
#2.4
#Re-write your function such that the checkerboard begins with a 0 instead.
checkers = checkerboard(8)
def reversealtboth(checkers):
    for i in range(0, len(checkers)):
        for j in range(0, len(checkers[0])):
            if (i+j)%2 ==1:
                checkers[i][j] =1
    return checkers
reversealtboth(checkers)
#3 The Expanding Universe
#You have now become fascinated with how dark energy is making galaxies ac-
#celerate away from us. Write a function that takes in a string and a number,
#and returns the string with the specified number of spaces inserted between each
#letter, simulating the expansion of space! For example:
universe = np.array(['galaxy', 'clusters'])
def expansion(universe, n):
    spaces = ' ' * n
    array = np.array([], dtype=str)
    for word in universe:
        array = np.append(array, spaces.join(word))
    return array
expansion(universe, 1)
expansion(universe, 2)
#4 Second-Dimmest Star
#While analyzing a dataset of star luminosities, you need to identify the second-
#dimmest star in each cluster. Write a function that takes a 2D NumPy array
#and returns an array containing only the second-smallest value in each column.
#For example:
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
stars = ([[1123, 1456, 1789, 1324, 1876],
[1567, 1987, 1678, 1405, 1589],
[1345, 1654, 1523, 1109, 1923],
[1298, 1890, 1367, 1784, 1432],
[1823, 1756, 1489, 1672, 1550]])
def secondDimmest(stars):
    secondsmallest = np.sort(stars, axis=0)
    return secondsmallest[1]
secondDimmest(stars)
([1298, 1654, 1489, 1324, 1550])