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

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

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

def zip_lists(ll1, ll2):
    curr_1 = ll1.head
    curr_2 = ll2.head
    while curr_1 and curr_2:
        list_1_next = curr_1.next
        list_2_next = curr_2.next
        curr_1.next = curr_2
        curr_2.next = list_1_next
        curr_1 = list_1_next
        curr_2 = list_2_next
    ll2.head = curr_2
    return ll1

if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")

    result = str(ll1)
    print(result)