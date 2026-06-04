'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

#**** Solution****
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = {}
        d2 = {}

        for char in magazine:
            d1[char] = d1.get(char, 0) + 1
                

        for char in ransomNote:
            d2[char] = d2.get(char, 0) + 1


        for x in d2:
            if x not in d1:
                return False
            if d2[x] > d1[x]:
                return False

        return True
            