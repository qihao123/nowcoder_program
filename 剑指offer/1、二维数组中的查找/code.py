# -*- coding:utf-8 -*-
class Solution:
    # array ¶þÎ¬ÁÐ±í
    def Find(self, target, array):
        row = len(array) - 1
        col = len(array[0]) -1
        i = row
        j = 0
        while j<=col and i>=0:
            if target<array[i][j]:
                i -= 1
            elif target>array[i][j]:
                j += 1
            else:
                return True
        return False
        # write code here