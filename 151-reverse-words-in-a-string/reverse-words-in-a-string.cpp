class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word, result;
        vector<string> words;

        while (ss >> word) words.push_back(word);
        reverse(words.begin(), words.end());

        for (const string& w : words) result += w + " ";
        if (!result.empty()) result.pop_back();

        return result;
    }
};