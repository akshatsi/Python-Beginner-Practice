class Solution:
    def printNumber(self):
        a = int(input(""))
        print(a)
        return
    
    def studentGrade(self, marks):
        if marks >= 90:
            print("A")
            
        elif marks >= 70:
            return 'B'
            
        elif marks >= 50:
            return 'C'
            
        elif marks >= 35:
            return 'D'
        else:
            return "Fail"
        return

a = int(input("enter marks: "))
Solution().studentGrade(a)