from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def set_head(self, head_node):
        self.head = head_node

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    # Push new item in the front of list.
    def push(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.set_head(node)

    def append(self, value):
        node = Node(value)
        current = self.head
        if not current:
            self.head = node
            return

        while current.get_next():
            current = current.get_next()

        current.set_next(node)

    #Return true if list contains the given value
    def contains(self, value):
        found = False
        current = self.head
        while current and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
            return found

    # Pop an item in the front of the list
    def pop(self):
        if self.head:
            self.head = self.head.get_next()
        else:
            raise IndexError("Unable to pop from empty list")

    # Delete all instances of value in list
    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                break
            else:
                prev = current
                current = current.get_next()

    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.get_next()
        return output