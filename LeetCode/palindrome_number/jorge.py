class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = x
        result = 0
        while(True):
            if z / 10 >= 1:
                y = z % 10
                result += y
                result *= 10
                z = int(z/10)
            else:
                y = z % 10
                result += y
                break

  
        if x == result:
            return True
        else:
            return False