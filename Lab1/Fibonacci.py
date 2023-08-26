def fib(k):
    if k <= 0:
        return []
    elif k == 1:
        return [0]
    elif k == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]
    for i in range(2, k):
        next_fib = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_fib)

    return fibonacci_sequence


k = int(input("Введіть кількість чисел Фібоначчі (k): "))
n = fib(k)
print(f"Перші {k} чисел Фібоначчі: {n}")
