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
    s1 = ""
    hash1 = simhash(s1)
    print(hash1)
    # print(hash1.hamming_distance(hash2), " ### ", hash1.similarity(hash2))