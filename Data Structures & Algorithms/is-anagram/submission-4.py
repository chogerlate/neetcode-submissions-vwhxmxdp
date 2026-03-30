class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this is character frequency problem obvisouly for easy we create Counter dict which cause O(n)
        s_count_dict = Counter(s)
        t_count_dict = Counter(t)
        return True if s_count_dict == t_count_dict else False