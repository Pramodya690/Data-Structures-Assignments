def hamming_distance(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

def approximate_pattern_matching(k, t, p):
    result = []
    m, n = len(t), len(p)

    for i in range(m - n + 1):
        substring = t[i:i + n]
        distance = hamming_distance(substring, p)

        if distance <= k:
            result.append(i)

    return result

# Input provided as a multiline string
input_data = """1 abcdabcd abcd
1 baaa abc
1 abcabcc abc
2 abcabcc abc
3 abcabcc abc
"""

# Processing the input
queries = []
for line in input_data.split('\n'):
    if line:
        k, t, p = line.split()
        queries.append((int(k), t, p))

# Output the results
for k, t, p in queries:
    positions = approximate_pattern_matching(k, t, p)
    print(len(positions), end=' ')
    for pos in positions:
        print(pos, end=' ')
    print()
