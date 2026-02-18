class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class SinglyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.len = 0
        prev = None

        if iterable is None:
            iterable = []

        for val in iterable:
            node = Node(val)
            if not self.head:
                self.head = node
            else:
                prev.next = node

            self.tail = node
            prev = node
            self.len += 1

    def __len__(self):
        return self.len

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

    def __repr__(self):
        return f"SinglyLinkedList([{', '.join([str(val) for val in self])}])"

    def __str__(self):
        return f"{' --> '.join([str(val) for val in self])}"

    def append_left(self, val):
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        self.len += 1

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            self.len += 1
            return

        self.tail.next = node
        self.tail = node
        self.len += 1

    def pop_left(self):
        if self.head is None:
            return

        val = self.head.val
        new_head = self.head.next
        self.head.next = None
        self.head = new_head
        self.len -= 1

        if self.head is None:
            self.tail = None

        return val

    def pop(self):
        if self.head is None:
            return

        val = self.tail.val

        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next

        if prev:
            prev.next = None
            self.tail = prev
        else:
            self.head = None
            self.tail = None

        self.len -= 1
        return val

    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0

    def insert(self, val, position):
        if self.head is None:
            self.append(val)
            return

        if position == 0:
            self.append_left(val)
            return

        if position == self.len:
            self.append(val)
            return

        if position > self.len or position < 0:
            raise Exception("Invalid Position")

        curr = self.head
        prev = None
        counter = 0
        while counter <= position:
            if counter == position:
                insert_node = Node(val)
                insert_node.next = curr
                prev.next = insert_node
                break

            prev = curr
            curr = curr.next
            counter += 1

        self.len += 1

    def remove(self, position):
        if self.head is None:
            return

        if position == 0:
            removed_val = self.pop_left()
            return removed_val

        if position == self.len - 1:
            removed_val = self.pop()
            return removed_val

        if position >= self.len or position < 0:
            return

        curr = self.head
        prev = None
        counter = 0
        while counter <= position:
            if counter == position:
                removed_val = curr.val
                next_node = curr.next
                prev.next = next_node
                self.len -= 1
                return removed_val

            prev = curr
            curr = curr.next
            counter += 1


if __name__ == "__main__":
    linked_list = SinglyLinkedList([1, 2, 3, 4, 5, 6])
    for node in linked_list:
        print(node)
    print("debug")
    print(len(linked_list))
    linked_list.insert(7, 5)
    print(linked_list.remove(2))
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print(linked_list.pop())
    print("debug")
