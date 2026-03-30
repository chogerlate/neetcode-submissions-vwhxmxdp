class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Problem analysis
        Repeating character:
        - variable to track the longest lenght
        - using 2 pointers for sliding windows
        - using Counter dict to check if it possible to replace the chacter with the dominant character in the windows..
        - How do we expand and shrink the windows???
            - if the windows is empty just expand them by increase the p2
            - if we expand the windows we create the key in counter dict with deafult to 1 when encounter the value 
            and change them dynamically as we navigate through the array, if the sum counts of the key which is not the dominant chracter exceeding "k" 
            we moving the p1 and decrease the count of the p1 associate key 
        """

        counter = defaultdict(int)
        p1, p2 = 0, 0 
        longest_lenght = 0

        def is_valid(counter: dict[int,int], k) -> bool:
            dominant_pair = (-1,-1)
            for key, value in counter.items():
                if value > dominant_pair[1] : 
                    dominant_pair = (key, value)
            
            non_dominant_count = 0
            for key, value in counter.items():
                if key is dominant_pair[0] :
                    continue
                non_dominant_count += value
            
            return True if non_dominant_count <= k else False

        def count(counter:dict[int,int]) -> int :
            return sum([value for value in counter.values()])

        while p2 < len(s) : 
            print(counter)
            counter[s[p2]] += 1
            if is_valid(counter, k):
                longest_lenght = max(longest_lenght, count(counter))
            else:
                counter[s[p1]] -= 1
                p1 += 1
            p2 += 1

        return longest_lenght
        