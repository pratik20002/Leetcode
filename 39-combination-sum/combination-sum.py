class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(remaining - candidates[i], combo, i)
                combo.pop()

        result = []
        candidates.sort()  
        backtrack(target, [], 0)
        return result