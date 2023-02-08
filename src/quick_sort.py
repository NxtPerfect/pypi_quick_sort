#!/usr/bin/env python3

def partition(array, start: int, end: int):
    # As pivot point we use the end of the array
    pivot = array[end]

    # pointer for greater element
    i = start - 1

    # go through the array and compare
    # each element with pivot
    for j in range(start, end):
        if array[j] <= pivot:
            # if element is greater than pivot
            # swap these elements
            i = i + 1

            # swapping elements
            (array[i], array[j]) = (array[j], array[i])

    # swap pivot with greater element, so that pivot is in the middle
    # to further divide the table in next recursive call
    (array[i + 1], array[end]) = (array[end], array[i + 1])

    return i + 1


def quick_sort(array, start: int, end: int):
    if start < end:
        # partitioning index, used to divide arrays into sub-arrays
        partition_index = partition(array, start, end)

        # left array
        quick_sort(array, start, partition_index - 1)

        # right array
        quick_sort(array, partition_index + 1, end)
