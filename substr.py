def find_longest_common_substring(s, t):
    max_length = 0
    result = (0, 0, 0)

    for i in range(len(s)):
        for j in range(len(t)):
            l = 0
            while (i + l < len(s)) and (j + l < len(t)) and (s[i + l] == t[j + l]):
                l += 1

            if l > max_length:
                max_length = l
                result = (i, j, l)

    return result

# Input reading
pairs = []
try:
    while True:
        line = input()
        if not line:
            break
        s, t = line.split()
        pairs.append((s, t))
except EOFError:
    pass

# Find the length of the longest common substring for each pair
results = []
for s, t in pairs:
    result = find_longest_common_substring(s, t)
    results.append(result)

# Output the results
for result in results:
    print(result[0], result[1], result[2])
