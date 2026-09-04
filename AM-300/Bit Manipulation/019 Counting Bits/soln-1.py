class Solution:
  def countBits(self, n: int) -> List[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
      count = 0
      curr = i
      while curr:
        curr &= curr - 1
        count += 1
      ans[i] = count
    return ans
  
# Brian Kernighan Iteration
# time -> O(n)
# space -> O(1)