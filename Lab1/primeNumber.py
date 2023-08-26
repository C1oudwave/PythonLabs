def isPrime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if any(number % i == 0 for i in range(2, int(number**0.5) + 1)):
        return False
    return True


def printPrimeNumbers():
    a, b = sorted(map(int, input("Введіть значення a та b через пробіл: ").split()))

    print(f"Прості числа між {a} і {b}:")
    prime_numbers = [number for number in range(a, b + 1) if isPrime(number)]
    print(*prime_numbers, sep=", ")

printPrimeNumbers()
