class Solution {
public:
    int countPairs(vector<int>& nums, int target) {
        size_t size = nums.size();

        if (!std::is_sorted(nums.begin(), nums.end())) {
            std::sort(nums.begin(), nums.end());
        }

        size_t i = 0;
        size_t j = size - 1;
        int pairs = 0;

        for (; i < j; ++i) {
            int sum = nums[i] + nums[j];
            if (sum < target) {
                pairs += (j - i);
            } else {
                --j;
                --i;  
            }
        }

        return pairs;
    }
};