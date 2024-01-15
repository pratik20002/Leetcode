class Solution {
public:
    string reverseWords(string s) {
        int left = 0;
        int right = 0;

        while(left < s.length()) {
            while (left < right || (left < s.length() && s[left] == ' ')) {
                ++left;
            }
            while (right < left || (right < s.length() && s[right] != ' ')) {
                ++right;
            }
            std::reverse(s.begin() + left, s.begin() + right);
        }
        return s;
    }
};