class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sorted_lists(list1, list2):
    stack1, stack2 = Stack(), Stack()

    while list1 is not None:
        stack1.push(list1.value)
        list1 = list1.next

    while list2 is not None:
        stack2.push(list2.value)
        list2 = list2.next

    head = None
    count = 0

    while not (stack1.is_empty() and stack2.is_empty()) and count < 50:
        if stack2.is_empty() or (not stack1.is_empty() and stack1.peek() <= stack2.peek()):
            new_value = stack1.pop()
        else:
            new_value = stack2.pop()

        new_value = max(min(new_value, 100), -100)

        new_node = ListNode(new_value)
        new_node.next = head
        head = new_node
        count += 1

    return reverse_linked_list(head)

def print_linked_list(head):
    values = []
    while head is not None:
        values.append(head.value)
        head = head.next

    print(" -> ".join(map(str, values)))

def create_linked_list():
    values = input("Enter values separated by space: ").split()
    values = [max(min(int(val), 100), -100) for val in values]  
    
    if not values or len(values) >= 50:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example usage
if __name__ == "__main__":
    print("Enter values for the 1st linked list:")
    list1 = create_linked_list()

    print("\nEnter values for the 2nd linked list:")
    list2 = create_linked_list()

    list1 = reverse_linked_list(list1)
    list2 = reverse_linked_list(list2)

    merged_list = merge_sorted_lists(list1, list2)

    print("\nMerged List:")
    print_linked_list(merged_list)
