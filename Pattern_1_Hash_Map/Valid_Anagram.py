class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) == len(t):
            for char in s:
                if char in d:
                    d[char] += 1
                else:
                    d[char] = 1

            for char2 in t:
                if char2 in d:
                    d[char2] -= 1
                else: return False

            for char3 in d:
                if d[char3] != 0:
                    return False
                else:
                    return True
                
s = "anagram"
t = "nagaram"
solution = Solution()
result = solution.isAnagram(s,t)
print(result)


#**********Solution 2**********class Solution:
def isAnagram(self, s: str, t: str) -> bool:
    d1 = {}
    d2 = {}
    if len(s) == len(t):
        for char in s:
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1
        print(d1)

        for char in t:
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = 1
        print(d2)
        
        for char in d1.keys():
            if char in d2 and d1[char] == d2[char]:
                del d2[char]

        if len(d2) != 0:
            return False
        else:
            return True
        