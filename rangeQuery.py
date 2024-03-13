import random
from tqdm import tqdm
from skipList import Node, SkipList
from collections import Counter
import timeit
from arrayOfSortedArray import arrayOfSortedArray
from binary_search import binary_search_left, binary_search_right

def rangeQuery_sortedArray(sorted_array, a, b):
    # 使用二分查找找到範圍開始和結束的索引
    start, end = 0, len(sorted_array) - 1
    while start < len(sorted_array) and sorted_array[start] < a:
        start += 1
    while end >= 0 and sorted_array[end] > b:
        end -= 1
    return sorted_array[start:end + 1] if start <= end else []

def rangeQuery_skipList(skip_list, a, b):
    result = []
    current = skip_list.header.forward[0]
    while current and current.key < a:
        current = current.forward[0]
    while current and current.key <= b:
        result.append(current.key)
        current = current.forward[0]
    return result

def rangeQuery_arrayOfSortedArray(aosa, a, b):
    result = []
    for array in aosa.arrays:
        if array:  # Ensure the sub-array is not empty
            # Find the range using binary search
            start_index = binary_search_left(array, a)
            end_index = binary_search_right(array, b)
            # Add the range [a, b] from the sub-array to the result
            for i in range(start_index, min(end_index, len(array))):
                if a <= array[i] <= b:
                    result.append(array[i])
    return result
  
def equivalent(multiset1, multiset2, description="Multisets"):
    if Counter(multiset1) == Counter(multiset2):
        return True  # Multisets是等价的
    else:
        # 引发带有更具体信息的异常
        raise ValueError(f"{description} are not equivalent")
    
def print_set(multiset):
    print(multiset)

if __name__ == '__main__':
    # Number of elements to generate
    #n = 2**20 - 1
    n = 2**5 - 1
    # Generate n random numbers
    random_numbers = [random.randint(0, n - 1) for _ in tqdm(range(n))]
    # Save the numbers to a file
    file_path = './random_numbers.txt'
    with open(file_path, 'w') as file:
        for number in tqdm(random_numbers):
            file.write(f'{number}\n')

    # Read the numbers from the file and store them in different data structures
    sortedArray = []
    skipList = SkipList(3, 0.5)
    aosa = arrayOfSortedArray()
    with open(file_path, 'r') as file:
        for line in tqdm(file):
            number = int(line.strip())
            sortedArray.append(number)
            skipList.insertElement(number)
            aosa.insert(number)
    sortedArray.sort()
    #print(f"\n*****Sorted Array******\n{sortedArray}")
    #skipList.displayList()
    aosa._print_structure()

    # Run range query
    numTrials = 10   
    a = random.randint(0, n - 1)
    ks = [ 2**i for i in range(0, 21)]
    for k in ks:
        b = a + k
        times_for_sortedArray = []
        times_for_skiplist = []
        times_for_arrayOfSortedArray = []

        for trial in range(numTrials):
            # append time for sortedArray, skipList, arrayOfSortedArray
            start_time = timeit.default_timer()
            rangeQueryResult_SortedArray = rangeQuery_sortedArray(sortedArray, a, b)
            times_for_sortedArray.append(timeit.default_timer() - start_time)

            start_time = timeit.default_timer()
            rangeQueryResult_SkipList = rangeQuery_skipList(skipList, a, b)
            times_for_skiplist.append(timeit.default_timer() - start_time)

            start_time = timeit.default_timer()
            rangeQueryResult_ArrayOfSortedArray = rangeQuery_arrayOfSortedArray(aosa, a, b)
            times_for_arrayOfSortedArray.append(timeit.default_timer() - start_time)
            
            ## print multisets
            #print(f"\nRange Query {a}~{b} on Sorted Array:")
            #print_set(rangeQueryResult_SortedArray)

            #print(f"\nRange Query {a}~{b} on Skip List:")
            #print_set(rangeQueryResult_SkipList)

            #print(f"\nRange Query {a}~{b} on ArrayOfSortedArray:")
            #print_set(rangeQueryResult_ArrayOfSortedArray)

            ##Equivalent test
            try:
                # 检查SortedArray和SkipList
                equivalent(rangeQueryResult_SortedArray, rangeQueryResult_SkipList, "Range query in SortedArray and SkipList")

                # 检查SortedArray和ArrayOfSortedArray
                equivalent(rangeQueryResult_SortedArray, rangeQueryResult_ArrayOfSortedArray, "Range query in SortedArray and SkipList")

                # 检查SkipList和ArrayOfSortedArray
                equivalent(rangeQueryResult_SkipList, rangeQueryResult_ArrayOfSortedArray, "Range query in SortedArray and SkipList")
            except ValueError as e:
                print(e)  # 打印错误信息
                break  # 退出循环

        avgTime_SortedArray = sum(times_for_sortedArray) / numTrials
        avgTime_SkipList = sum(times_for_skiplist) / numTrials
        avgTime_ArrayOfSortedArray = sum(times_for_arrayOfSortedArray) / numTrials
        print(f"\nAverage Time for Range Query {a} ~ {a}+{k} on Sorted Array: {avgTime_SortedArray} seconds")
        print(f"Average Time for Range Query {a} ~ {a}+{k} on Skip List: {avgTime_SkipList} seconds")
        print(f"Average Time for Range Query {a} ~ {a}+{k} on ArrayOfSortedArray: {avgTime_ArrayOfSortedArray} seconds")








        #rangeQuerySortedArray = rangeQuery_sortedArray(sortedArray, a, b)
        #print(f"\n*****Range Query{a}~{b}******{rangeQuerySortedArray}")
        #runRangeQueryAvgTime_SortedArray = runRangeQueryAvgTime(rangeQuery_sortedArray(sortedArray, a, b))
        #runRangeQueryAvgTime_SortedArray = runRangeQueryAvgTime(rangeQuery_sortedArray, sortedArray, a, b)
        #print(f"Average Time for Range Query {a}~{b}: {runRangeQueryAvgTime_SortedArray} seconds")
