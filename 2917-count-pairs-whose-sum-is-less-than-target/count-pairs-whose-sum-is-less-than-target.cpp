class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        int size = nums.size();
        std::sort(nums.begin(), nums.end());
        int i = 0;
        int j = size - 1;
        int pairs = 0;
        while (i < j) {
            int sum = nums[i] + nums[j];
            if (sum < target) {
                pairs += (j - i);
                i++;
            } else {
                j--;
            }
        }
        
        return pairs;
    }
};