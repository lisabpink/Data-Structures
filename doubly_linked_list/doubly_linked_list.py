"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # create a new_node
        new_node = ListNode(value, None, None)
        # check if the DLL is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length = self.length + 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if not self.head:
            self.head = None
        else:
            new_head = self.head.next
            new_head.prev = None
            self.lenth -= 1

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.insert_after = None
            self.tail = new_node
            self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if not self.tail:
            if not self.head:
                return None
        else:
            current = self.head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous = self.tail
            previous.next = None
            self.length -= 1
            return current

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        current = self.head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # decrement length of DLL
        self.length -= 1

        # if DLL is empty, there is nothing to delete, we should return
        if not self.head and not self.tail:
            return

        # if DLL has one element, remove it by
        # setting head and tail pointers to None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value


dll = DoublyLinkedList()
dll.add_to_head(7)
print(dll.head.value)
dll.add_to_tail(12)
print(dll.tail.value)
dll.add_to_tail(21)
print(dll.tail.value)
print(dll.__len__())
print(dll.head.value)
print(dll.tail.value)
x = dll.remove_from_tail()
print(x.value)
print(dll.__len__())
