'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        l=[]
        for i in s:
            l.append(i[::-1])
        return " ".join(l)
