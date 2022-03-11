# Efficient but long
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # storage
        uncommon = []
        
        #splits
        s1_split = s1.split()
        s2_split = s2.split()
        
        
        # maps of counts for s1 an s2
        s1_counts = {w: 0 for w in s1_split}
        for w in s1_split:
            s1_counts[w] += 1
        
        s2_counts = {w: 0 for w in s2_split}
        for w in s2_split:
            s2_counts[w] += 1
        
        # check if a word in uncommon
        for w in s1_split:
            if s1_counts[w] == 1 and w not in s2_counts.keys():
                uncommon.append(w)
                
        for w in s2_split:
            if s2_counts[w] == 1 and w not in s1_counts.keys():
                uncommon.append(w)
                
        return uncommon
        
 # Short
 class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # storage
        uncommon = []
        
        # join
        s = s1 + " " + s2
        s = s.split()
        
        # map for counts
        counts = {w: 0 for w in s}
        for w in s:
            counts[w] += 1
        
        # check for words with count 1
        uncommon = [w for w in set(s) if counts[w] == 1]
                
        return uncommon
 
