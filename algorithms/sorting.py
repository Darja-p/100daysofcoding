# sorting algorithms
import time

# bubble sort
def bubble(a_list):
    if len(a_list)>=2:
        for i in range(len(a_list)-1):
            if a_list[i]> a_list[i+1]:
                a_list[i+1], a_list[i] =a_list[i], a_list[i+1]
        a_list[:-1] = bubble(a_list[:-1])
    return a_list

# bubble sort
def bubble2(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list)-i-1):
            if a_list[j]> a_list[j+1]:
                a_list[j+1], a_list[j] =a_list[j], a_list[j+1]
    return a_list


# INSERTION SORT

def insert_sort(a_list):
    for i in range(len(a_list)-1):
        key = a_list[i+1]
        while a_list[i]>key:
            a_list[i+1], a_list[i] = a_list[i], key
            i -= 1
    return a_list


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key

    return array



a = [4,6,3,9,2,1,8,10,1,3]

start_time2 = time.time()
print(bubble2(a))
print(f"Execution of bubble sort 2 (optimized) :{time.time() - start_time2:.10f}")

start_time1 = time.time()
print(bubble(a))
print(f"Execution of bubble sort 1 (with recursion):{time.time() - start_time1:.10f}")

start_time3 = time.time()
print(insert_sort(a))
print(f"Execution of insertion sort 1:{time.time() - start_time3:.10f}")

start_time4 = time.time()
print(insertionSort(a))
print(f"Execution of insertion sort 2 (first moving elements to the right, then placing the current el):{time.time() - start_time1:.10f}")