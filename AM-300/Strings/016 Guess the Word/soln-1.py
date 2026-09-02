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
            # Pick any word at random from remaining candidates
            guess_word = words[random.randint(0, len(words) - 1)]

            # Get feedback from master API
            matches = master.guess(guess_word)
            if matches == 6:
                return

            # Keep ONLY candidates that share EXACTLY matches count with guess_word
            words = [w for w in words if count_matches(guess_word, w) == matches]

# Randomized Match Filtering Strategy
# time -> O(N * L) per guess where N is candidate count and L is word length
# space -> O(N)