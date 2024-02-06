'''
-----------------------------------------------------------------------
File: heapsort.py
Creation Time: Jan 23rd 2024, 8:09 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''
def swap(array, i, j):
    """
    Swaps elements at indices i and j in the given array.
    """
    array[i], array[j] = array[j], array[i]

def sift_down(array, i, upper):
    """
    Performs the sift-down operation in a heap.
    """
    while True:
        left, right = i * 2 + 1, i * 2 + 2
        if max(left, right) < upper:
            if array[i] >= max(array[left], array[right]):
                break
            elif array[left] > array[right]:
                swap(array, i, left)
                i = left
            else:
                swap(array, i, right)
                i = right
        elif left < upper:
            if array[left] > array[i]:
                swap(array, i, left)
                i = left
            else:
                break
        elif right < upper:
            if array[right] > array[i]:
                swap(array, i, right)
                i = right
            else:
                break
        else:
            break

def heap_sort(array):
    """
    Sorts the given array using the Heap Sort algorithm.
    """
    if any(isinstance(element, str) for element in array):
        # Handle the case where the list contains strings
        print("Cannot perform heap sort on a list containing strings.")
        raise TypeError
    
    for j in range((len(array) - 2) // 2, -1, -1):
        sift_down(array, j, len(array))

    for end in range(len(array) - 1, 0, -1):
        swap(array, 0, end)
        sift_down(array, 0, end)

    return array