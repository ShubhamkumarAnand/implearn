import hashlib

class BloomFilter:
    def __init__(self, m, k): # m = length of the bit array, k = number of hash function
        self.m = m
        self.k = k
        self.data = [0]*m
        self.n = 0
    def insert(self, element):
        if self.k == 1:
            hash1 = h1(element) % self.m
            self.data[hash1] = 1
        elif self.k == 2:
            hash1 = h1(element) % self.m
            hash2 = h2(element) % self.m
            self.data[hash1] = 1
            self.data[hash2] = 1
        self.n += 1
    def search(self, element):
        if self.k == 1:
            hash1 = h1(element) % self.m
            if self.data[hash1] == 0:
                return "Not in Bloom Filter"
        elif self.k == 2:
            hash1 = h1(element) % self.m
            hash2 = h2(element) % self.m
            if self.data[hash1] == 0 or self.data[hash2] == 0:
                return "Not in Bloom Filter"
        prob = (1.0 - ((1.0 - 1.0/self.m)**(self.k*self.n))) ** self.k
        return "Might be in Bloom Filter with false positive probability "+str(prob)

# Hash Function for the bloom filter

def h1(w):
    h = hashlib.md5(w)
    return hash(h.digest().encode('base64')[:6])%10

def h2(w):
    h = hashlib.sha256(w)
    return hash(h.digest().encode('base64')[:6])%10

# Testing the bloom filter

>>> bf = BloomFilter(10, 1)
>>> bf.insert("Hello")
>>> bf.data
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

>>> bf.search("Hello")
'Might be in Bloom Filter with false positive probability 0.1'
>>> bf.search("No Way")
'Not in Bloom Filter'
>>> bf.search("ge")
'Might be in Bloom Filter with false positive probability 0.1'

>>> bf = BloomFilter(10, 2)
>>> bf.insert("Hello")
>>> bf.data
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0]

>>> bf.search("Hello")
'Might be in Bloom Filter with false positive probability 0.0361'
>>> bf.search("ge")
'Not in Bloom Filter'