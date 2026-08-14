class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out=''
        for word in words:
            v=0
            for i in word:
                v+=weights[ord(i)-97]
            out+=chr(122-(v%26))
        return out