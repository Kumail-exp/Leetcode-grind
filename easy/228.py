class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        out=[]
        start=nums[0]
        prev=nums[0]
        for val in nums:
            if val==prev:
                continue
            if(val-prev!=1):
                if(start==prev):
                    out.append(f"{start}")
                else:
                    out.append(f"{start}->{prev}")
                start=val
            prev=val
        if(start==prev):
            out.append(f"{start}")
        else:
            out.append(f"{start}->{prev}")
        return out
                