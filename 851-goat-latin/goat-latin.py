class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        goatSentence = []
        for idx, word in enumerate(words):
            if word[0] in "AEIOUaeiou":
                word += "ma" + (idx + 1) * "a"
            else:
                word = word[1:] + word[0] + "ma" + (idx + 1) * "a"
            goatSentence.append(word)
        
        return " ".join(goatSentence)
        