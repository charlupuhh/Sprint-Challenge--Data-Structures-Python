class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.oldest_index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.oldest_index] = item
            if self.oldest_index == self.capacity - 1:
                self.oldest_index = 0
            else:
                self.oldest_index += 1

    def get(self):
        return self.storage