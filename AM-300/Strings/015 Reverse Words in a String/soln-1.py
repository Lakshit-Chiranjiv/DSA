class Solution:
    def reverseWords(self, s: str) -> str:
        r = " ".join(reversed(s.split()))
        return r

# reverseWords_split_and_join
# time -> O(N)
# space -> O(N)