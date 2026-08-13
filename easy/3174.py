class Solution:
    def clearDigits(self, s: str) -> str:
        chars=[]
        for i in s:
            if i in "1234567890":
                chars.pop()
            else:
                chars.append(i)
        return "".join(chars)

