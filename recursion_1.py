# 1)
def reverse_print_string(s):
    # Базовий випадок: якщо рядок порожній, не потрібно нічого друкувати.
    if s == "":
        return

    # Рекурсивний випадок: вивести останній символ рядка і викликати функцію зі скороченим рядком.
    print(s[-1], end='')
    reverse_print_string(s[:-1])

# Приклад використання:
input_string = "tiger"
reverse_print_string(input_string)







