class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def swap_pairs_recursive(head):
    if not head or not head.next:
        return head

    next_pair = head.next.next # None
    new_head = head.next # 2
    head.next.next = head # 1 - 2 - 1
    head.next = swap_pairs_recursive(next_pair) # 2

    return new_head

def create_linked_list():
    num_nodes = int(input("Введіть кількість узлів (від 0 до 100): "))
    while num_nodes < 0 or num_nodes > 100:
        num_nodes = int(input("Кількість узлів має бути від 0 до 100. Введіть ще раз: "))

    head = None
    for i in range(num_nodes):
        value = int(input(f"Введіть значення для вузла {i + 1}: "))
        new_node = Node(value)
        if not head:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = new_node

    return head

# Створення списку вузлів з введенням з клавіатури та обмін пар вузлів
head_node = create_linked_list()
if head_node:
    new_head = swap_pairs_recursive(head_node)
    while new_head:
        print(new_head.value, end=" -> ")
        new_head = new_head.next
else:
    print("Список вузлів пустий.")