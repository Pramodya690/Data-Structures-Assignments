class PhoneBookManager:
    def __init__(self):
        self.phone_book = {}

    def process_queries(self, queries):
        results = []
        for query in queries:
            command, *params = query.split()
            if command == "add":
                number, name = params
                self.phone_book[number] = name
            elif command == "del":
                number = params[0]
                if number in self.phone_book:
                    del self.phone_book[number]
            elif command == "find":
                number = params[0]
                results.append(self.phone_book.get(number, "not found"))
        return results

# Input reading
n = int(input())
queries = [input() for _ in range(n)]

# Phone book manager initialization
manager = PhoneBookManager()

# Process queries and get the results
results = manager.process_queries(queries)

# Output the results
for result in results:
    print(result)
