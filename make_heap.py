def heapify(arr):
    swaps = []
    n = len(arr)

    def sift_down(i):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] < arr[min_index]:
            min_index = left_child

        if right_child < n and arr[right_child] < arr[min_index]:
            min_index = right_child

        if i != min_index:
            swaps.append((i, min_index))
            arr[i], arr[min_index] = arr[min_index], arr[i]
            sift_down(min_index)

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i)

    return swaps


# Input processing
n = int(input())
arr = list(map(int, input().split()))

# Convert array into a heap using heapify
swap_operations = heapify(arr)

# Output the result
print(len(swap_operations))
for swap in swap_operations:
    print(swap[0], swap[1])
