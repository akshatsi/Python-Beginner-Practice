class solution:
    def rectpattern(self, N):
        for i in range(N):
            for j in range(N):
                print("x", end = " ")
            print()
        return
    
    def rightangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print("x", end = " ")
            print()
        return
    def rightnum(self, N):
        for i in range(N):
            for j in range(i + 1):
                print(j + 1, end = " ")
            print()
        return
    def rightsamenum(self, N):
        for i in range(N):
            for j in range(i+1):
                print(i+1, end = " ")
            print()
        return
    
    def reverseright(self, N):
        for i in range(N):
            for j in range(N-i, 0, -1):
                print("x", end = " ")
            print()
        return
    def reverserightnum(self, N):
        for i in range(N):
            for j in range(N-i):
                print(j+1, end = " ")
            print()
        return
    def pyramid(self, N):
        for i in range (N):
            for j in range (N-i-1):
                print(" ", end = " ") # for space
            for k in range (2*i+1): # for stars in odd numbers
                print("*", end = " ")
            print()
        return
    def revpyramid(self, N):
        for i in range (N):
            for j in range (i):
                print(" ", end = " ") 
            for k in range (2*(N-i)-1): 
                print("*", end = " ")
            print()
        return
    def diamond(self, N):
        for i in range (N):
            for j in range (N-i-1):
                print(" ", end = " ")
            for k in range(2*i+1):
                print("*", end = " ")
            print()
        for i in range (N-1):
            for j in range(i+1):
                print(" ", end = " ")
            for k in range(2*(N-i-1)-1):
                print("*", end = " ")
            print()
        return
    def halfdiamond(self, N):
            for i in range (N):
                for j in range(i +1):
                    print("*", end = " ")
                print()
            for i in range(N-1):
                for j in range (N-i-1):
                    print("*", end = " ")
                print()
            return
    def rightbinarynum(self, N):
        start = 1
        for i in range(N):
            if i % 2 ==0:
                start = 1
            else: 
                start = 0
            for j in range(i+1):
                print(start, end = " ")
                start = 1- start
            print()
        return
    def ditch(self, N):
        for i in range(1, N + 1):
            for j in range(1, i + 1): #numbers increasing
                print(j, end="")

            # Middle spaces (only if not last row)
            spaces = 2 * (N - i)
            for s in range(spaces):
                print(" ", end="")

            # Right decreasing numbers
            for k in range(i, 0, -1):
                print(k, end="")

            print()


        return
    def increasingright(self, N):
        num = 1
        for i in range (N):
            for j in range(i + 1):
                print(num, end = " ")
                num += 1
            print()
        return
    def alphasameright(self, N):
        for i in range (N):
            for j in range (i+1):
                print( chr(65 + i), end = " ")
            print()
        return
    def alpharight(self, N):
        for i in range (N):
            for j in range (i+1):
                print( chr(65 + j), end = " ")
            print()
        return
    def reverserightalpha(self, N):
        for i in range(N):
            for j in range(N-i-1):
                print(chr(65 + j), end = " ")
            print()
a = 5
solution().rectpattern(a)
print("\n")
solution().rightangle(a)
print("\n")
solution().rightnum(a)
print("\n")
solution().rightsamenum(a)
print("\n")
solution().reverseright(a)
print("\n")
solution().reverserightnum(a)
print("\n")
solution().pyramid(a)
print("\n") 
solution().revpyramid(a)
print("\n")
solution().diamond(a)
print("\n")
solution().halfdiamond(a)
print("\n")
solution().rightbinarynum(a)    
print("\n")
solution().ditch(a)
print("\n")
solution().increasingright(a)
print("\n")
solution().alpharight(a)
print("\n")
solution().alphasameright(a)
print("\n")
solution().reverserightalpha(a)