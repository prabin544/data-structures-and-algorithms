from code_challenges.linked_list.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        has_index = 0
        for char in key:
            has_index += ord(char)

        has_index *= 599

        has_index = has_index % self.size
        return has_index

    def add(self, key, value):
        hash_index = self.hash(key)

        if not self.buckets[hash_index]:
            self.buckets[hash_index] = LinkedList()

        bucket = self.buckets[hash_index]

        bucket.insert([key, value])


    def get(self, key):
        hash_index = self.hash(key)

        if self.buckets[hash_index] is None:
            return None

        current = self.buckets[hash_index].head

        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        return None


    def contains(self, key):
        hash_index = self.hash(key)

        if self.buckets[hash_index] is None:
            return False

        current = self.buckets[hash_index].head

        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False