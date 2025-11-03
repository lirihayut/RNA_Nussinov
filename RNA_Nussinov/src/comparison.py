def compare_structures(s1, s2):
    if len(s1)!=len(s2):
        return None
    matches = sum(1 for a,b in zip(s1,s2) if a==b)
    return matches/len(s1)*100
