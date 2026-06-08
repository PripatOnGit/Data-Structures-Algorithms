'''
Problem Link: https://leetcode.com/problems/word-pattern/description/
Approach: Hash Map
To solve this problem, we can use a hash map (dictionary) to store the mapping between letters in the pattern and words in the string s. We will iterate through both the pattern and the list of words simultaneously, checking for consistency in the mapping.
1. Split the string s into a list of words.
2. Check if the length of the pattern matches the number of words. If not, return False.
3. Create an empty hash map to store the letter-to-word mapping.
4. Iterate through the pattern and the list of words together:
   a. For each letter in the pattern and the corresponding word in the list:
      i. If the letter is already in the hash map, check if it maps to the same word. If not, return False.
      ii. If the letter is not in the hash map, check if the word is already mapped to a different letter. If so, return False.
      iii. If there are no conflicts, add the mapping of the letter to the word in the hash map.
      5. If we successfully iterate through the entire pattern and list of words without conflicts, return True.
      Time Complexity: O(n), where n is the length of the pattern (or the number of words in s). We iterate through both the pattern and the list of words once.
      Space Complexity: O(m), where m is the number of unique letters in the pattern (or unique words in s). In the worst case, this could be O(n) if all letters and words are unique.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split()
        word_map = {}
        for i in range(len(pattern)):   
            letter = pattern[i]
            word = word_list[i]
        
            # Conflict 1: This letter was already mapped to a DIFFERENT word
            if letter in word_map and word_map[letter] != word:
                return False 
                #f"Conflict: Letter '{letter}' cannot map to both '{word_map[letter]}' and '{word}'."
            
            # Conflict 2: A different letter is already using this word
            if word in word_map.values() and letter not in word_map:
                return False 
                #f"Conflict: The word '{word}' is already taken by another letter."
            
        # If no conflicts, save the mapping
            word_map[letter] = word
        
        return True
    

    
'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space. '''