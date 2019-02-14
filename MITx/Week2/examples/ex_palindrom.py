def to_chars(s):
    
    s = s.lower()
    ans = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for c in s:
        if c in alphabet:
            ans += c
    
    return ans

def isPalindrome(s_char):

    if len(s_char) <= 1:
        return True
    
    else:
        return s_char[0] == s_char[-1] and isPalindrome(s_char[1:-1])



print(isPalindrome(to_chars('ablelba')))