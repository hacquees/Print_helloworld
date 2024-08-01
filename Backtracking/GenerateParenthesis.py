"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

def generateParenthesis(n):
    def gg(i,j,s):
        if len(s)==2*n:
            r.append(s)
            return 
        if i<n:
            gg(i+1,j,s+"(")
        if j<i:
            gg(i,j+1,s+")")
    r=[]
    gg(0,0,"")
    return r

print(generateParenthesis(int(input())))
    