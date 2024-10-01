class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charMap = {}
        for idx, c in enumerate(order):
            charMap[c] = idx

        print(charMap)

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j>= len(words[i + 1]):
                    return False

                if words[i][j] != words[i+1][j]:
                    if charMap[words[i][j]] > charMap[words[i+1][j]]:
                        return False

                    break

        return True
