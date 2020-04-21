class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        else:
            rst = ""
            analyze = self.countAndSay(n-1)
            
            for i in range(len(analyze)):
                
                for j in range(i,len(analyze)):
                    
                    if analyze[i] != analyze[j]:
                        
                        rst += str(len(analyze[i:j])) + analyze[i]
                        i = j
                if len(set(analyze[i:]))==1:
                    rst += str(len(analyze[i:]))+ analyze[i]
                    break
            return rst
