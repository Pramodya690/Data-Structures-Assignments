class HashTable:
    def __init__(self, m):
        self.m = m
        self.p = 10**9 + 7
        self.x = 263
        self.buckets = [[] for _ in range(m)]

    def hash_function(self, string):
        result = 0
        for i in range(len(string)):
            result = (result * self.x + ord(string[i])) % self.p
        return result % self.m

    def add(self, string):
        hash_value = self.hash_function(string)
        if string not in self.buckets[hash_value]:
            self.buckets[hash_value].insert(0, string)

    def delete(self, string):
        hash_value = self.hash_function(string)
        if string in self.buckets[hash_value]:
            self.buckets[hash_value].remove(string)

    def find(self, string):
        hash_value = self.hash_function(string)
        return "yes" if string in self.buckets[hash_value] else "no"

    def check(self, i):
        return " ".join(reversed(self.buckets[i]))

# Input reading
m = int(input())
n = int(input())
queries = [input().split() for _ in range(n)]

# Hash table initialization
hash_table = HashTable(m)

# Process queries and get the results
results = []
for query in queries:
    command = query[0]
    if command == "add":
        hash_table.add(query[1])
    elif command == "del":
        hash_table.delete(query[1])
    elif command == "find":
        results.append(hash_table.find(query[1]))
    elif command == "check":
        results.append(hash_table.check(int(query[1])))

# Output the results
for result in results:
    print(result)
