class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = ''.join(l for l in licensePlate if l.isalpha()).lower()
        c = math.inf
        ans= ''
        for word in words:
            n = 0
            if len(word) >= len(letters):
                for s in set(letters):
                    if s not in word or letters.count(s) > word.count(s):
                        n = math.inf
                        break

                for char in set(word):
                    if char in letters:
                        n += word.count(char) - letters.count(char)
                    else:
                        n += word.count(char)
            else: 
                n = math.inf
            if n < c:
                ans = word
                c = n
        
        return ans