class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        # edge case
        if len(rating) == 3 and sorted(rating) == rating:
            return 1
        elif len(rating) == 3 and sorted(rating, reverse=True) == rating:
            return 1
        elif len(rating) == 3 and sorted(rating) != rating:
            return 0
        
        # teams count
        count = 0
        # iterate
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                for k in range(j+1, len(rating)):
                    if rating[i]<rating[j]<rating[k] or rating[i]>rating[j]>rating[k]:
                        # print((i,j,k), (rating[i], rating[j], rating[k]))
                        count += 1
        return count
