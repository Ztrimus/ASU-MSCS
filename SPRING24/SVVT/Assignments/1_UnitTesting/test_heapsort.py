'''
-----------------------------------------------------------------------
File: test_heapsort.py
Creation Time: Jan 23rd 2024, 8:51 pm
Author: Saurabh Zinjad
Developer Email: saurabhzinjad@gmail.com
Copyright (c) 2023-2024 Saurabh Zinjad. All rights reserved | https://github.com/Ztrimus
-----------------------------------------------------------------------
'''
import random
import pytest
from heapsort import heap_sort, swap, sift_down

# Test cases for swap function
def test_swap():
    arr = [1, 2, 3, 4]
    swap(arr, 0, 3)
    assert arr == [4, 2, 3, 1]

# Test cases for sift_down function
def test_sift_down():
    arr = [3, 5, 1, 4, 2]
    sift_down(arr, 0, len(arr))
    assert arr == [5, 4, 1, 3, 2]

# Test case for sorting an empty list
def test_heapsort_empty_list():
    assert heap_sort([]) == []

# Test case for sorting a list with a single element
def test_heapsort_single_element():
    assert heap_sort([5]) == [5]

# Test case for sorting a list with all elements in ascending order
def test_heapsort_sorted_list():
    arr = [1, 2, 3, 4, 5]
    assert heap_sort(arr) == sorted(arr)

# Test case for sorting a list with all elements in descending order
def test_heapsort_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    assert heap_sort(arr) == sorted(arr)

# Test case for sorting a list with repeated elements
def test_heapsort_list_with_duplicates():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert heap_sort(arr) == sorted(arr)

# Test case for sorting a list with negative numbers
def test_heapsort_list_with_negative_numbers():
    arr = [-5, 2, -8, 0, 3]
    assert heap_sort(arr) == sorted(arr)

# Test case for sorting a list with fractional numbers
def test_heapsort_list_with_fractional_numbers():
    arr = [2.5, 1.0, 3.5, 2.0]
    assert heap_sort(arr) == sorted(arr)

# Test case with boolean values
def test_heapsort_list_with_boolean_values():
    arr = [True, False, True]
    assert heap_sort(arr) == sorted(arr)

# Test case for sorting a list with mixed data types (integers and strings)
def test_heapsort_mixed_data_types():
    with pytest.raises(TypeError):
        heap_sort([1, 'apple', 3, 'banana', 2, 'orange'])

# Test case for sorting a large list to check for performance
def test_heapsort_large_list():
    large_list = list(range(10**6, 0, -1))
    sorted_list = list(range(1, 10**6 + 1))
    assert heap_sort(large_list) == sorted_list

# Test case for sorting a list with NaN and Infinity values
def test_heapsort_list_with_nan_and_infinity():
        arr = [float('inf'), 5, float('-inf'), 3, float('nan'), 1]
        with pytest.raises(AssertionError):
            assert heap_sort(arr) == sorted(arr)

# Test case for sorting a list with generator
def test_heapsort_list_with_generater():
    def generate_random_data(size, seed=None):
        random.seed(seed)
        for _ in range(size):
            yield random.randint(1, 100)

    sorted_data = sorted(generate_random_data(10000, seed=42))
    assert heap_sort(list(generate_random_data(10000, seed=42))) == sorted_data

# Test case for sorting a list with objects
def test_heapsort_list_with_objects():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __lt__(self, other):
            if self.x < other.x:
                return True
            elif self.x == other.x:
                return self.y < other.y
            return False

    points = [Point(3, 5), Point(1, 1), Point(2, 4)]
    with pytest.raises(TypeError):
        assert heap_sort(points) == [Point(1, 1), Point(2, 4), Point(3, 5)]

from copy import deepcopy
# Test case for sorting a list with mutable elements
def test_heapsort_for_mutable_elements():
    class Node:
        def __init__(self, value, children=None):
            self.value = value
            self.children = children or []

    nodes = [Node(1), Node(2, children=[Node(3), Node(4)]), Node(5)]
    original_nodes = deepcopy(nodes)
    with pytest.raises(TypeError):
        heap_sort(nodes)

    # Check if original nodes were not modified
    assert original_nodes[0].value == 1
    assert original_nodes[1].value == 2
    assert original_nodes[1].children[0].value == 3
    assert original_nodes[1].children[1].value == 4
    assert original_nodes[2].value == 5

    # Check sorted nodes
    assert nodes[0].value == 1
    assert nodes[1].value == 2
    assert nodes[1].children[0].value == 3
    assert nodes[1].children[1].value == 4
    assert nodes[2].value == 5
