class Solution(object):
    def hIndex(self, citations):
        citation_ordened = sorted(citations, reverse=True)
        h = 0
        for i, num_citations in enumerate(citation_ordened):
            num_articles = i + 1
            if num_citations >= num_articles:
                h = max(h, num_articles)
            else:
                break
        return h
    
solucion = Solution()

nums=[3,0,6,1,5]
print(solucion.hIndex(nums))