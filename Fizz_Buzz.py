class Solution(object):
    def fizzBuzz(self, n):
        out = []
        for i in range(1,n+1):
            res = ""
            if i%3 == 0:
                res+="Fizz"
            if i%5 == 0:
                res+="Buzz"
            if res == "":
                res+=str(i)
            out.append(res)
        return out

n = 3
n = 5
n = 15
solution = Solution()
out = solution.fizzBuzz(n)

print(out)