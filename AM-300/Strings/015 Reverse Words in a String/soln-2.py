class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Convert to list to simulate a mutable character array and strip spaces
        chars = []
        i, n = 0, len(s)
        while i < n:
            if s[i] != " ":
                if chars:
                    chars.append(" ")
                while i < n and s[i] != " ":
                    chars.append(s[i])
                    i += 1
            i += 1

        # Helper function to reverse a slice in-place
        def reverse_range(left: int, right: int):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        # Step 2: Reverse the entire array
        reverse_range(0, len(chars) - 1)

        # Step 3: Reverse each individual word back
        start = 0
        for end in range(len(chars) + 1):
            if end == len(chars) or chars[end] == " ":
                reverse_range(start, end - 1)
                start = end + 1

        return "".join(chars)
    
# reverseWords_two_pointer_inversion
# time -> O(N)
# space -> O(N)
# Same approach as soln-1 just without using in-built functions.