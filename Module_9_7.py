def check_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if check_prime(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

##Пример:
result = sum_three(2, 3, 6)
print(result)
