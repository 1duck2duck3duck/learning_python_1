# 1
for n in range(2,11):
    print(n)

# 2
n = 1

while n < 10:
    n += 1
    print(n)

#3

def doubles(x):
    result = x * 2
    return result

x =int(input("Please enter num for doubles: "))
y = 2
n = 0

for n in range(2,5):
    x = doubles(x)
    print(x)
    
