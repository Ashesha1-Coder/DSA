#Given two strings s and t, return true if t is an 
#anagram (anagram is a word in which same letters are present but order is different like anagram nagaram)
# of s, and false otherwise.
class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False
        comparison_set =set(s)
        for i in comparison_set:
            if(s.count(i)!=t.count(i)):
                return False
        return set(s)==set(t)

        