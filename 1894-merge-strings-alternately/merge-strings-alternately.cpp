#include <string>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        int j = word1.length();
        int y = word2.length();
        std::string mergedWord;
        int i = 0, x = 0;
        
        while (i < j && x < y) {
            mergedWord += word1[i];
            mergedWord += word2[x];
            i++;
            x++;
        }

        if (i < j) {
            mergedWord += word1.substr(i);
        } else if (x < y) {
            mergedWord += word2.substr(x);
        }

        return mergedWord;
    }
};
