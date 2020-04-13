# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # hash(key) % 12
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # hash_value = 5381
        # for i in key:
        #     hash_value = ((hash_value << 5) + hash_value) + i
        # return hash_value
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash_mod(key)
        # value = LinkedPair(key, value)

        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            if self.storage[index].key == key:
                self.storage[index].value == value
            else:
                next_pair = self.storage[index].next_pair
                while next_pair is not None:
                    if next_pair.key == key:
                        next_pair.value = value
                    elif next_pair == None:
                        next_pair = LinkedPair(key, value)
                    else:
                        next_pair = next_pair.next

        # if self.storage[hash_key] is not None:
        #     print('collision warning')
        # self.storage[hash_key] = LinkedPair(key, value)

    def remove(self, key):
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index] = None
            else:
                next_pair = self.storage[index].next

                while next_pair is not None:
                    if next_pair.key == key:
                        next_pair = None
                    else:
                        next_pair = next_pair.next
        else:
            print(f'this {key} does not exist')

        # index = self._hash_mod(key)
        # self.storage[index] = None

    def retrieve(self, key):
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                next_pair = self.storage[index].next
                while next_pair:
                    if next_pair.key == key:
                        return next_pair.value
                    else:
                        next_pair = next_pair.next
        else:
            return None

        # index = self._hash_mod(key)
        # if self.storage[index] is None:
        #     return None
        # return self.storage[index].value
        # pass

    def resize(self):
        # pass
        old_storage = self.storage
        self.capacity *= 2

        self.storage = [None] * self.capacity
        for pair in old_storage:
            if pair is not None:
                self.insert(pair.key, pair.value)


if __name__ == "__main__":
    ht = HashTable(3)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
