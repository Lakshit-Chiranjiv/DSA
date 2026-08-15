class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    prefix = []
    for chars in zip(*strs):
      if len(set(chars)) == 1:
        prefix.append(chars[0])
      else:
        break
    return "".join(prefix)