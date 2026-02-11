import time

numbers = list(range(1, 1000000))

# Lambda function
double_lambda = map(lambda x: x * 2, numbers)

start = time.time()
list(map(lambda x: x * 2, numbers))
print(time.time() - start)

# Standard function
def double_standard(x):
    return x * 2

start = time.time()
map(double_standard, numbers)
print(time.time() - start)


# 3.504753112792969e-05
# 2.384185791015625e-05