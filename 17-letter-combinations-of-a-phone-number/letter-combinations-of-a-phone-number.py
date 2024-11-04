class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # Initialize a queue with an empty combination
        queue = deque([""])

        # Iterate over each digit in `digits`
        for digit in digits:
            letters = phone_map[digit]
            # Process current queue size to only expand combinations of the current level
            for _ in range(len(queue)):
                current_combination = queue.popleft()  # Take the current combination
                # Append each letter for the current digit to form new combinations
                for letter in letters:
                    queue.append(current_combination + letter)
        
        # Convert deque to list and return all combinations
        return list(queue)
