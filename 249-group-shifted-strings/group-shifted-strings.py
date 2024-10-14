class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouping_dict = defaultdict(list)

        for string in strings:
            if len(string) == 1:
                grouping_dict[(-1)].append(string)
            
            else:
                char_diff = []
                i = 1
                while i < len(string):
                    char_diff.append(
                        (ord(string[i]) - ord(string[i-1])) % 26
                    )
                    i += 1
                
                grouping_dict[tuple(char_diff)].append(string)

        return grouping_dict.values()
