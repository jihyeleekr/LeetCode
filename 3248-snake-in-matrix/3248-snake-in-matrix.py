class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        ans = 0
        for com in commands:
            if com == 'DOWN':
                ans += n
            elif com == "UP":
                ans -= n
            elif com == "RIGHT":
                ans += 1
            else:
                ans -= 1
        return ans

        