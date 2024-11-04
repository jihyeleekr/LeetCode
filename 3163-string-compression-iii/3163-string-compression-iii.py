class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        if word != None:
            sub = word[0]
            count = 1
            if len(word) == 1:
                return "1" + word

            for i in range(1, len(word)):
                if count < 9:
                    if i == len(word) - 1:
                        if word[i] == sub:
                            comp += str(count + 1) + sub
                        else:
                            comp += str(count) + sub
                            comp += "1" + word[i]
                    else:
                        if word[i] == sub:
                            count += 1

                        else:
                            comp += str(count) + sub
                            sub = word[i]
                            count = 1
                else:
                    comp += str(count) + sub
                    if i == len(word) - 1:
                        comp += "1" + word[i]
                    else:
                        sub = word[i]
                        count = 1

        return comp

            
        
        