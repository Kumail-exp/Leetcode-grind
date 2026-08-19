revs = set()
for i in range(100000):
    revs.add(i + int(str(i)[::-1]))

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        return num in revs