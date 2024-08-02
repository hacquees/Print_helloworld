"""Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 """
 
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=dict(Counter(t))
        i,j=0,0
        c=len(d)
        min_len=float('inf')
        start=0
        while j<len(s):
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    c-=1
            
            if c==0:
                while c==0:
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        start = i
                    if s[i] in d:
                        d[s[i]]+=1
                        if d[s[i]]>0:
                            c+=1

                    i=i+1
            j+=1

        if min_len == float('inf'):
            return ""
        return s[start:start + min_len]
 


s=input()
t=input()
ob=Solution()
print(ob.minWindow(s,t))
                

        