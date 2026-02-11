# Use filter with lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # print the list of the filter object to see the result

# [2, 4, 6, 8]

nombres= ["Pedro", "Juan", "Pablo", "Manuel", "Jose"]
evens2 = filter(lambda x: 'n' in x == 0, nombres)
print(list(evens2))