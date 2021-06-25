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

    def kth_from_end(self, k):
        list_head = self.head
        count = 0
        while list_head != None:
           list_head = list_head.next
           count += 1
        if k > count:
            print("Out of Range")
        elif k == count:
            print("Same Length")
        elif k < 0:
            print("negative Number")
        elif k == self:
            print("Linked list needs to be greater than 1")
        list_head = self.head
        for i in range(0, count - k):
            list_head = list_head.next
        return list_head.value


if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")

    result = str(ll1)
    print(result)