class RNASequence:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.length = len(sequence)
    
    def can_pair(self, i, j):
        b1, b2 = self.sequence[i], self.sequence[j]
        return (b1=='A' and b2=='U') or (b1=='U' and b2=='A') \
               or (b1=='G' and b2=='C') or (b1=='C' and b2=='G') \
               or (b1=='G' and b2=='U') or (b1=='U' and b2=='G')
