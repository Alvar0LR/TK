import random
import string
import time
# Generate a dictionary with elements of the form 'XX': number.
NUMBER_ITEMS = 1000000
items = {
    ''.join(random.choices(string.ascii_uppercase, k=2)): random.randint(1, 100)
    for _ in range(NUMBER_ITEMS)
}

# Standard function (extra definition step)
def sort_standard(item):
    return item[1]

print('Standard')
start = time.time()
sorted_items_standard = sorted(items, key=sort_standard)
print(time.time() - start)
print(sorted_items_standard[:5])
print()

# Lambda function
print('Lambda')
start = time.time()
sorted_items_lambda = sorted(items, key=lambda x: x[1])
print(time.time() - start)
print(sorted_items_lambda[:5])
print()

# Standard
# 0.00011610984802246094
# ['OA', 'VA', 'XA', 'IA', 'BA']
# Lambda
# 0.00011014938354492188
# ['OA', 'VA', 'XA', 'IA', 'BA']