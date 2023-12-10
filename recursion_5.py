def power(x, n):
    if not (-100 < x < 100) or not (-2 ** 31 <= n <= 2 ** 31 - 1) or not (n % 1 == 0):
        return "Обмеження не виконані. Перевірте вхідні дані."

    def power_recursive(x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            return power_recursive(x * x, n // 2)
        else:
            return x * power_recursive(x * x, (n - 1) // 2)

    if n < 0:
        x = 1 / x
        n = -n

    return power_recursive(x, n)

# Приклад виклику функції для x = 2, n = -3
x = 2
n = 3
result = power(x, n)
print(f"{x} піднесене до ступеня {n} дорівнює {result}")