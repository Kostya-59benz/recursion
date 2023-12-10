def count_steps_recursive(n):
    if n < 1 or n > 45:
        return "Недійсне значення для n. n повинно бути від 1 до 45"
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_steps_recursive(n - 1) + count_steps_recursive(n - 2)

# Приклад виклику функції для n = 4 (кількість кроків)
n = 4
unique_combinations = count_steps_recursive(n)
print(f"Кількість унікальних комбінацій для досягнення вершини з {n} кроків: {unique_combinations}")