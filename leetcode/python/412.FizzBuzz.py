class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = [str(i) for i in range(1, n + 1)]

        for i in range(n):
            index = i + 1
            tmp = ""
            if index % 3 == 0:
                tmp += "Fizz"
            if index % 5 == 0:
                tmp += "Buzz"
            
            if tmp != "":
                ret[i] = tmp
        
        return ret