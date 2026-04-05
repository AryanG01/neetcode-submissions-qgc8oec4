class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}

        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        
        sorted_dic = sorted(dic.items(), key=lambda x: -x[1])

        res = []

        for i,x in enumerate(sorted_dic[:k]):
            res.append(x[0])

        return res    