class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while(left < right):
            if(numbers[left] + numbers[right] == target):
                return [left + 1, right + 1]
            elif(target - numbers[left] > numbers[right]):
                left += 1
            else:
                right -= 1
