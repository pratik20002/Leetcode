class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wrd_ptr = abbr_ptr = 0

        while wrd_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                steps = 0

                if abbr[abbr_ptr] == '0':
                    return False
                
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    steps = steps * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                
                wrd_ptr += steps
            
            else:
                if word[wrd_ptr] != abbr[abbr_ptr]:
                    return False
                
                wrd_ptr += 1
                abbr_ptr += 1
            
        return wrd_ptr == len(word) and abbr_ptr == len(abbr)