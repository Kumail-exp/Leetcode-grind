class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs=0
        mxc=0
        for i in s:
            if i=='L':
                chairs-=1
            else:
                chairs+=1
            mxc=chairs if chairs>mxc else mxc
        return mxc