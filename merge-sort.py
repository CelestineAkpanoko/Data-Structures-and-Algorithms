#!/usr/bin/env python3

''' A python script that implements merge sort algorithm.'''

from array import array


def mergesort(arr):
    '''mergesort: recursively half the array'''
    n = len(arr) # get the length of the array
    if n == 1: # recursion base condition
        return arr
    
    mid = n//2 # get the mid index of the array
    leftArr = arr[:mid] # initializes the left array
    rightArr = arr[mid:n] # initializes the right array

    leftArr = mergesort(leftArr) # recursively half the left array
    rightArr = mergesort(rightArr) # recursively half the right array

    return merge(leftArr, rightArr) # merge both arrays

def merge(arr_x, arr_y):
    '''merge: an helper function to combine the arrays'''
    arr_z = [] # the new array to merge in
    i = j = 0 # initializes index for both left anf right arrays
    n_x = len(arr_x) #the number of elements in the left array
    n_y = len(arr_y) # the number of elements in the right array

    while i < n_x and j < n_y:
        if arr_x[i] > arr_y[j]: # checks if the left element is greater 
            arr_z.append(arr_y[j]) # then adds the right array element in the new array
            j += 1 # increases the index of the right array
        else:
            arr_z.append(arr_x[i]) # adds the left array element in the new array
            i += 1 # increases the index of the left array
    
    arr_z.extend(arr_x[i:])
    arr_z.extend(arr_y[j:])

    return arr_z


def main():
    import random
    import time

    arrInt = []
    i = 1000

    while i > 0:
        value = random.randint(1,10000)
        arrInt.append(value)
        i -= 1
    start_time = time.time()
    unsorted = arrInt
    sorted = mergesort(unsorted)
    # print("Sorted array: ", sorted)

    print("It took {}".format(time.time() - start_time),"Seconds")

main()

    