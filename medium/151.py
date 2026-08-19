class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip().split(" ")
        out=[]
        for i in range(len(s)-1,-1,-1):
            if s[i]:
                out.append(s[i])
        return ' '.join(out)