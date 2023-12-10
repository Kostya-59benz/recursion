# 3)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Приклад виклику функції для підрахунку F(n) для n = 10
n = 10
result = fibonacci(n)
print(f"F({n}) = {result}")