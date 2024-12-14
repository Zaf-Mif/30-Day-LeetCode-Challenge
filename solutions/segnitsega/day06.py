class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd_palindrome = expand_around_center(i, i)
            # Even-length palindrome
            even_palindrome = expand_around_center(i, i + 1)
            
           
            longest = max(longest, odd_palindrome, even_palindrome, key=len)
        
        return longest
