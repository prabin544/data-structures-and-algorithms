from stacks_and_queue.queues.queue import Node, Queues

def breadthFirst(tree):
    if tree.root == None:
        return []

    queue = Queues()
    queue.enqueue(tree.root)
    result = []

    while not queue.isEmpty():
        front = queue.dequeue()
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)

        result.append(front.value)
    return result
        
