class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise Exception('Stack is Empty')
        popped = self.top.value
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top is None:
            raise Exception('Stack is Empty')
        return self.top.value

    def isEmpty(self):
        return self.top == None





#         if self.top is None:
#             raise Exception("Stack is empty")
#         popped = self.top.value
#         self.top = self.top.next
#         return popped

#     def peek(self):

#         if self.top is None:
#             raise Exception("Stack is empty")
#         return self.top.value

#     def isEmpty(self):
#         return self.top == None

# if __name__ == "__main__":
#     pass