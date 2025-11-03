class NussinovDP:
    def __init__(self, rna_seq):
        self.rna = rna_seq
        self.N = [[0]*self.rna.length for _ in range(self.rna.length)]
        self.structure = ['.']*self.rna.length

    def fill_matrix(self):
        n = self.rna.length
        min_loop = 3
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                scores = [self.N[i+1][j], self.N[i][j-1]]
                if j-i > min_loop and self.rna.can_pair(i,j):
                    scores.append(self.N[i+1][j-1]+1)
                scores += [self.N[i][k]+self.N[k+1][j] for k in range(i+1,j)]
                self.N[i][j] = max(scores)

    def traceback(self, i=0, j=None):
        if j is None:
            j = self.rna.length-1
        if i>=j:
            return
        elif self.N[i][j]==self.N[i+1][j]:
            self.traceback(i+1,j)
        elif self.N[i][j]==self.N[i][j-1]:
            self.traceback(i,j-1)
        elif self.rna.can_pair(i,j) and self.N[i][j]==self.N[i+1][j-1]+1:
            self.structure[i]='('
            self.structure[j]=')'
            self.traceback(i+1,j-1)
        else:
            for k in range(i+1,j):
                if self.N[i][j]==self.N[i][k]+self.N[k+1][j]:
                    self.traceback(i,k)
                    self.traceback(k+1,j)
                    break

    def get_structure(self):
        self.traceback()
        return ''.join(self.structure)

    def get_max_pairs(self):
        return self.N[0][self.rna.length-1]
