class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, node=None):
        self.head = node

    def insert(self, value):

        node = Node(value)
        node.next = self.head
        self.head = node
        return self

    def append(self, value):

        node = Node(value)
        
        if self.head is None:
            self.head = node
            return

        last = self.head

        while (last.next):
            last = last.next

        last.next = node
        return last

    def includes(self, value):

        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):

        string = ""

        current = self.head

        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next

        string += f" None "

        return string

if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")

    result = str(ll1)
    print(result)