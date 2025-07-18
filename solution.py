# Valid Anagram

def isAnagram(self, s, t):
    if len(s) != len(t):
            return False
        
    s_list = [0] * 26
    t_list = [0] * 26

    for i in range(len(s)):
        s_list[ord(s[i]) - ord('a')] += 1
        t_list[ord(t[i]) - ord('a')] += 1
        
    if s_list == t_list:
        return True
    else:
        return False
