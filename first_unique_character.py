#given a string, find the first non-repeating
#character and return the index. If not, return -1 
#'leetcode' -> 0
#'loveleetcode' -> 2
from collections import Counter 
s = 'leetcode'
class Solution(object):
    def firstUniqChar(self, s):


        character_map = Counter(list(s))
        for ind, c in enumerate(s):
            if character_map[c] == 1:
                print(ind) 
        return -1

