class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    if not strs:
      return ""

    first = strs[0]
    for i, char in enumerate(first):
      for s in strs[1:]:
        if i == len(s) or s[i] != char:
          return first[:i]

    return first

# Vertical Scanning
# time -> O(S)
# space -> O(1)