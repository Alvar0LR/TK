

# Sort a list of tuples by the second element
data = [(1, 3), (2, 1), (4, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

# [(2, 1), (4, 2), (1, 3)]
data2 = ['Pepe','Juan','Maria', 'Antonio']
sorted_data2 = sorted(data2, key=lambda x: x[-1])
print(sorted_data2)
