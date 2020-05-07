class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = 0
        self.hash_table = [None] * self.capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        load = self.storage / self.capacity
        load_factor = 0.7

        if load > load_factor:
            self.capacity = self.capacity * 2
            self.resize()

        self.storage += 1
        index = self.hash_index(key)
        node = self.hash_table[index]

        if node is None:
            self.hash_table[index] = HashTableEntry(key, value)
            return

        prev = None
        cur = node

        while cur is not None:
            if cur.key == key:
                cur.value = value
                return
            prev = cur
            cur = cur.next

        prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        load = self.storage / self.capacity
        load_factor = 0.2

        if load > load_factor:
            self.capacity = self.capacity // 2
            self.resize()

        index = self.hash_index(key)
        node = self.hash_table[index]
        while True:
            # get to the end
            if node.key == key:
                node.value = None
                return
            elif node.next is None:
                return
            else:
                node = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.hash_table[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

        old_hash_table = self.hash_table
        new_array = [None] * self.capacity
        self.hash_table = new_array

        self.storage = 0

        #  iterate through old hash table and checking to see if it's not empty
        for index in old_hash_table:
            node = index
            while node is not None:
                self.put(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
