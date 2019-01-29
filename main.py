

############################## 1 ##############################

start_num = 999
s = 0

while start_num != 0:
    if start_num % 5 == 0 :
        s += start_num
    elif start_num % 3 == 0:
        s += start_num
    start_num -= 1

print s

############################## 2 ##############################

fib = 1
new_fib = 1
prev_fib = 1
fib_sum = 0

while new_fib < 4000000:
    if fib % 2 == 0:
        fib_sum += fib
    new_fib = prev_fib + fib
    prev_fib = fib
    fib = new_fib
print fib_sum

############################## 3 ##############################


def is_prime(x):
    copy = 1
    while copy != x:
        if x%copy == 0:
            if copy != x and copy != 1:
                return 0
        copy += 1
    return 1


def mul_list(x):
    ret = 1
    for i in x:
        ret *= i
    return ret

num = 600851475143
div = 1
number = 0
factors = []
if is_prime(num):
    print num
else:
    while div != int(num/2):
        if num % div == 0:
            if is_prime(div):
                factors.append(div)
        number = mul_list(factors)
        if number == num:
            break
        div = div + 1
print factors[-1]

############################## 4 ##############################


def is_poly(x):
    num_str = str(x)
    if len(num_str) % 2 == 0:
        if num_str[0:len(num_str)/2] == num_str[-1:len(num_str)/2-1:-1]:
            return 1
    else:
        if num_str[0:int(len(num_str)/2)] == num_str[-1:int(len(num_str)/2):-1]:
            return 1
    return 0
num = 999*999


def largest_pol(x):
    while x:
        if is_poly(x):
            for i in range(999)[-1:1:-1]:
                if x % i == 0:
                    return x
        x -= 1
print largest_pol(num)
