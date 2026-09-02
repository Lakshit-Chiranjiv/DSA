# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def count_matches(w1: str, w2: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        while words:
            best_word = min(
                words,
                key=lambda w1: max(
                    sum(1 for w2 in words if count_matches(w1, w2) == i)
                    for i in range(6)
                ),
            )

            matches = master.guess(best_word)
            if matches == 6:
                return

            words = [w for w in words if count_matches(best_word, w) == matches]

# Minimax Match Filtering
# time -> O(N^2 * L) per step where N is word count and L is word length
# space -> O(N)