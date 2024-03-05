import heapq

def assign_jobs(n, m, processing_times):
    threads = [(0, i) for i in range(n)]  # Initialize threads with start time and index
    heapq.heapify(threads)  # Convert the list to a min heap

    result = []

    for i in range(m):
        start_time, thread_index = heapq.heappop(threads)
        result.append((thread_index, start_time))
        new_start_time = start_time + processing_times[i]
        heapq.heappush(threads, (new_start_time, thread_index))

    return result

# Input reading
n, m = map(int, input().split())
processing_times = list(map(int, input().split()))

# Assign jobs and get the result
result = assign_jobs(n, m, processing_times)

# Output the result
for thread_index, start_time in result:
    print(f"{thread_index} {start_time}")
