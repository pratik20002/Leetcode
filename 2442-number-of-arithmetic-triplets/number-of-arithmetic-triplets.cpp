class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        std::vector<bool> visited(201, false);
        for (int x : nums) {
            visited[x] = true;
        }
        int ans = 0;
        for (int x : nums) {
            ans += visited[x + diff] && visited[x + 2 * diff];
        }
        return ans;
    }
};