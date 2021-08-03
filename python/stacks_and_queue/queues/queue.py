class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Queues:
    def __init__(self, front=None, rear= None):
        self.front = front
        self.rear = rear


    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):

        if self.front is None:
            raise Exception("Queue is empty")

        dequed = self.front.value
        self.front = self.front.next
        return dequed

    def peek(self):
        if self.front is None:
            raise Exception("Queue is empty")

        return self.front.value

    def isEmpty(self):
        return self.front == None

    if __name__ == "__main__":
        pass