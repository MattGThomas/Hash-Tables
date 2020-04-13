storage = self.storage
        self.capacity *= 2

        self.storage = [None] * self.capacity
        for pair in old_storage:
            if pair is not None:
                self.insert(pair.key, pair.value)
