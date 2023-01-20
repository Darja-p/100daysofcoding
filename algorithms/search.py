import time


# linear search
def search_linear(a_list, a):
    for i in range(len(a_list)):
        if a_list[i] == a:
            print(f"It's a {i + 1} item in a list")


# binary search
def bi_search(a_list, a):
    mid = len(a_list) // 2
    if a_list[mid] == a:
        return mid
    elif mid > a:
        for i in range(mid):
            if a_list[i] == a:
                return i
    else:
        for i in range(mid + 1, len(a_list)):
            if a_list[i] == a:
                return i


# binary search 2
def bi_search2(a_list, start, end, a):
    while start <= end:
        mid = (start + end) // 2
        if a_list[mid] == a:
            return mid
        elif a_list[mid] > a:
            end = mid - 1
        else:
            start = mid + 1
    return start


# binary search 3 with recursion
def bi_search3(a_list, start, end, a):
    mid = (start + end) // 2
    if a_list[mid] == a:
        return mid
    elif a_list[mid] > a:
        return bi_search3(a_list, start, mid - 1, a)
    else:
        return bi_search3(a_list, mid + 1, end, a)


start_time1 = time.time()
search_linear(sorted([1, 4, 7, 8, 9, 22, 3, 9, 556, 2]), 9)
print(f"Execution of linear search:{time.time() - start_time1:.10f}")

start_time2 = time.time()
print(bi_search(sorted([1, 4, 7, 8, 9, 22, 3, 9, 556, 2]), 9))
print(f"Execution of binary 1 search:{time.time() - start_time2:.10f}")

start_time3 = time.time()
print(bi_search2(sorted([1, 4, 7, 8, 9, 22, 3, 9, 556, 2]), 0, len([1, 4, 7, 8, 9, 22, 3, 9, 556, 2]) - 1, 9))
print(f"Execution of binary 2 search:{time.time() - start_time3:.10f}")

start_time4 = time.time()
print(bi_search3(sorted([1, 4, 7, 8, 9, 22, 3, 9, 556, 2]), 0, len([1, 4, 7, 8, 9, 22, 3, 9, 556, 2]) - 1, 9))
print(f"Execution of binary 2 search:{time.time() - start_time4:.10f}")