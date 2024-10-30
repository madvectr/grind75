#! /usr/bin/env python

# Questions:
# We are looking for duplicates - hash table (improve perf/tradeoff space)
# Empty array
# Array with 2 elements
# Input: nums List[num], Output: bool

from collections import defaultdict
from typing import DefaultDict, List


def containsDuplicates(nums: List[int]) -> bool:
  table: DefaultDict = defaultdict(int) # dict to hold the count of each element in the array, defaulting absent keys to 0
  for num in nums:
    if table[num] == 1:
      return True 
    table[num] += 1
  return False


#Time: 8 Mins
# LC submission: https://leetcode.com/problems/contains-duplicate/submissions/1438217911