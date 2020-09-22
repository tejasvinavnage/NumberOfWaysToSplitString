#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 00:16:08 2020

@author: tejasvinavnage
"""

class Solution:
  def numWays(self, s):
    self.total = 0
    def func(string, index, a, b):
      if index == len(string):
          return
      else:
          if a and b:
              # print(a, b, string[index:], a!=b!=string[index:])
              c = string[index:]
              self.total += (0, 1)[a+b!=b+c and c+a!=b+c]
              return
          for i in range(index+1, len(string)):
              if not a:
                  func(string, i, string[index: i], b)
              elif not b:
                  func(string, i, a, string[index: i])
              else:
                # print(a, b, string[index:], a!=b!=string[index:])
                c = string[index:]
                self.total += (0, 1)[a+b!=b+c and c+a!=b+c]
    func(s, 0, None, None)
    return self.total


s = "xzxzx"
z = Solution()
print(z.numWays(s))