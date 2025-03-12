import numpy as np
crossproduct = np.matrix([vector, array1, array2])
vector = np.array(['i', 'j', 'k'])
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
np.dot(array1, array2)

def anglebetweenvectors(array1, array2):
    dot = np.dot(array1, array2)
    def magnitude(array):
        sqs = 0
        for i in range(0, len(array)):
            sqs +=(array[i])**2
        mag = np.sqrt(sqs)
        return mag
    bottom = magnitude(array1)*magnitude(array2)
    cosine = dot/bottom
    angle = np.arccos(cosine)
    return angle*(180/np.pi)
anglebetweenvectors(array1, array2)