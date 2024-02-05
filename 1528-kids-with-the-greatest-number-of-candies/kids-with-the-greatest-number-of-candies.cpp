class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandies = *max_element(candies.begin(), candies.end());
        vector<bool> result;
        result.reserve(candies.size());

        for (int candy : candies) {
            result.push_back(candy + extraCandies >= maxCandies);
        }

        return result;
    }
};