class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ind=[]
        for i in range(len(words)):
            if x in words[i]:
                ind.append(i)
        return ind