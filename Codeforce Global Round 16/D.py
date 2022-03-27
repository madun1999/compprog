import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp(): 
    # one integer
    return int(input())
def input_list():
    # list of integers
    return list(map(int,input().split()))
def input_string():
    # list of characters
    s = input()
    return list(s[:len(s) - 1])
def input_int_gen():
    # integer generator 
    return map(int,input().split())

# https://towardsdatascience.com/how-to-implement-merge-sort-algorithm-in-python-4662a89ae48c
def merge_sort(list):
    # 1. Store the length of the list
    list_length = len(list)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return list, 0

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition, left_res = merge_sort(list[:mid_point])
    right_partition, right_res = merge_sort(list[mid_point:])

    merged, merge_res = merge(left_partition, right_partition)
    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merged, left_res + right_res + merge_res


# 6. takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0
    res = 0
    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        if left[i] >= right[j]:
            # output is populated with the lesser value
            output.append(left[i])
            # 10. Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
            res += len(left) - i
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output, res
# Codeforces Global Round 16 D
from bisect import bisect_left
tests = inp()
for _ in range(tests):
    n, m = input_int_gen()
    a = input_list()
    sorted_a = sorted(a)
    splits = []
    holds = []

    for i in range(1, n):
        k = sorted_a[m*i-1]
        t = bisect_left(sorted_a, k)
        splits.append(k)
        holds.append(min(m*i - t, m))
    # print(splits, holds)
    splited_a = [[] for _ in range(n)]
    actual_hold = [0 for _ in range(n-1)]
    for i in a:
        t = bisect_left(splits, i)
        while t < len(splits) and i == splits[t] and actual_hold[t] >= holds[t]:
            t += 1
        splited_a[t].append(i)
        if t < len(splits) and i == splits[t]:
            actual_hold[t] += 1
    # print(splited_a)
    res = sum(merge_sort(x)[1] for x in splited_a)
    print(res)



        



