n = 1000
total = 0

def get_sum(num):
    return sum(int(i) for i in str(num))

for i in range(1, n + 1):
    total += get_sum(i)

print(total)
