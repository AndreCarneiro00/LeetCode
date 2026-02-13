class Node:
    def __init__(self, val, next_node=None, prev=None):
        self.val = val
        self.next = next_node
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, lst: list):
        self.head = None
        self.tail = None
        prev = None

        for val in lst:
            node = Node(val)
            if not self.head:
                self.head = node
                self.tail = node
            else:
                node.prev = prev
                self.tail = node
                prev.next = node

            prev = node


if __name__ == "__main__":
    linked_list = DoublyLinkedList([1, 2, 3])
    print("debug")