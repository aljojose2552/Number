total_sum = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        total_sum += x

# Print the result
print("The sum of all multiples of 3 or 5 below 1000 is:", total_sum)