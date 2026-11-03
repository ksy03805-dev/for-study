fruits = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange", "banana"]
fruit_count = {}

for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

print(fruit_count)
