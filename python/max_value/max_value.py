from stacks_and_queue.queues.queue import Node, Queues

def max_value(queue):

    max_value = 0

    while not queue.isEmpty():
        front = queue.dequeue()
        if front > max_value:
            max_value = front
    return max_value