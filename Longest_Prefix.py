class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        try:
            if not strs:
                return ""

            if len(strs) ==1:
                return strs[0][0]
            # for each letter check if all letters are the same if so count up one if not return count
            match=''
            for i in range(len(strs[0])):
                for j in range(len(strs)):
                    if strs[0][i]!=strs[j][i]:
                        return match

                match=match+strs[0][i]
            return match
        except IndexError:
            return match
  
    def longest(self, strs):
        if not strs:
            return ""
        # Sort the list of strings
        strs.sort()
        # Compare the first and last string in the sorted list
        first = strs[0]
        last = strs[-1]
        i = 0
        # Find the common prefix between first and last string
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
