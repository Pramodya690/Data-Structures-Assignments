from collections import deque

def process_packets(buffer_size, packets):
    current_time = 0
    buffer = deque()
    result = []

    for arrival_time, processing_time in packets:
        # Process packets that have already arrived and finished processing
        while buffer and buffer[0][1] <= current_time:
            _, _ = buffer.popleft()

        # Check if the buffer is full
        if len(buffer) < buffer_size:
            start_time = max(current_time, arrival_time)
            finish_time = start_time + processing_time
            buffer.append((arrival_time, finish_time))
            result.append(start_time)
            current_time = finish_time  # Update current time to the finish time of the processed packet
        else:
            result.append(-1)

    return result

# Input
buffer_size, num_packets = map(int, input().split())
packets = [tuple(map(int, input().split())) for _ in range(num_packets)]

# Output
result = process_packets(buffer_size, packets)
for r in result:
    print(r)
