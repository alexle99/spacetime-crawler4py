class simhash:
    #Constructor
    def __init__(self, tokens='', hashbits=128):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens)

    #ToString function
    def __str__(self):
        return str(self.hash)

    #Generating simhash values
    def simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self._string_Hash(x) for x in tokens]:
            for i in range(self.hashbits):
                Bitmask = 1 << i
                if t & Bitmask:
                    v[i] += 1
                else:       
                    v[i] -= 1
        Fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                Fingerprint += 1 << i
        return Fingerprint
    
    #Seeking Hamming distance
    def hamming_distance(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hashbits) - 1)
        tot = 0
        while x:
            tot += 1
            x &= x - 1
        return tot

    #Find similarity
    def similarity(self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b:
            return b / a
        else:
            return a / b

    #Generating hash values for source (a built-in hash for a variable length version of Python)
    def _string_Hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hashbits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x

if __name__ == '__main__':
    s1 = 'This is a test string for testing'
    hash1 = simhash(s1.split())

    s2 = 'This is a test string for testing also'
    hash2 = simhash(s2.split())

    s3 = 'nai nai ge xiong cao'
    hash3 = simhash(s3.split())

    s4 = 'this is a water fire earth air the dogs are very nice and the dogs look ugly'
    hash4 = simhash(s4.split())

    s5 = 'poop peep toot'
    hash5 = simhash(s5.split())
    
    s6 = 'poop peep dump'
    hash6 = simhash(s6.split())

    print("PRINT HASHES", hash1,hash2,hash3,hash4,hash5,hash6)

    print(hash1.hamming_distance(hash2), " ### ", hash1.similarity(hash2))
    if hash1.similarity(hash2) > 0.9:
        print("THEY ARE SIMILAR")
    print(hash1.hamming_distance(hash3), " @@@ ", hash1.similarity(hash3))
    print("POOP SIMILARITY: ")
    print(hash1, hash4)
    print(hash1.hamming_distance(hash4), "AND", hash1.similarity(hash4))
    print("@@@@@@@@")
    print(hash5.hamming_distance(hash6), " | ", hash5.similarity(hash6))