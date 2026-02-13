class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return f"[{self.val}, {self.next}]"


class SinglyLinkedList:
    def __init__(self, lst: list):
        self.head = None
        prev = None

        for val in lst:
            node = Node(val)
            if not self.head:
                self.head = node
            else:
                prev.next = node

            prev = node


if __name__ == "__main__":
    linked_list = SinglyLinkedList([1, 2, 3, 4, 5, 6])
    print("debug")
