class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join([str(c) for c in digits])
        s = int(s)+1
        return list(str(s))