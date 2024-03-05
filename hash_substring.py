def rabin_karp(pattern, text):
    results = []

    # Define prime number for hashing
    prime = 101

    # Calculate hash of the pattern and the first substring in the text
    pattern_hash = 0
    text_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * prime + ord(pattern[i])) % (10**9 + 7)
        text_hash = (text_hash * prime + ord(text[i])) % (10**9 + 7)

    # Calculate prime^(len(pattern)) for rolling hash calculation
    prime_power = pow(prime, len(pattern), 10**9 + 7)

    # Iterate through the text to find occurrences of the pattern
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and text[i:i + len(pattern)] == pattern:
            results.append(i)

        # Update rolling hash for the next substring
        if i < len(text) - len(pattern):
            text_hash = (text_hash - ord(text[i]) * prime_power) % (10**9 + 7)
            text_hash = (text_hash * prime + ord(text[i + len(pattern)])) % (10**9 + 7)

    return results

# Input reading
pattern = input()
text = input()

# Find occurrences using Rabin-Karp algorithm
occurrences = rabin_karp(pattern, text)

# Output the results
if occurrences:
    print(" ".join(map(str, occurrences)))
else:
    print("Pattern not found")
