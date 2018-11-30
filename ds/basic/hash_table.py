class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, self.size)

        if self.slots[hash_value]:  # existed
            if self.slots[hash_value] == key:  # replace
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, self.size)
                while self.slots[next_slot] and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, self.size)

                if self.slots[next_slot]:  # existed
                    self.data[next_slot] = data  # replace
                else:  # not existed
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
        else:  # not existed
            self.slots[hash_value] = key
            self.data[hash_value] = data

    def hash_function(self, key, size):
        return key % size

    # linear probing
    def rehash(self, old_hash, size):
        return (old_hash+1) % size

    def get(self, key):
        start_slot = self.hash_function(key, self.size)

        data = None
        stop = False
        found = False
        pos = start_slot

        while self.slots[pos] and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, self.size)
                if pos == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

if __name__ == '__main__':

    H=HashTable()
    H[54]="cat"
    H[26]="dog"
    H[93]="lion"
    H[17]="tiger"
    H[77]="bird"
    H[31]="cow"
    H[44]="goat"
    H[55]="pig"
    H[20]="chicken"

    print(H.slots)
    print(H.data)
