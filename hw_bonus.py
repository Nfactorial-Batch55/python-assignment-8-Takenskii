"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:

    sequence_val = 0

    for nums in my_list:
        if nums - 1 not in my_list:
            current_val = nums
            sequence_val = 1
            
            while current_val + 1 in my_list:
                current_val += 1
                sequence_val += 1

    return sequence_val

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
pass

"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
    # write your code here
    res = 0
    my_list.sort()
    if len(my_list) == 1:
        return None
        
    else: 
        for i in range(1, len(my_list)):
            if my_list[0] != 1:
                res = 1
            elif my_list[i] - my_list[i - 1] == 2:
                res = my_list[i] - 1

    return res

print(find_missing([1]))
pass


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    # write your code here
    for i in range(0, len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                return my_list[i]
    return -1    

print(find_duplicate([1, 1]))
pass


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

def group_anagrams(words: list[str]) -> list[list[str]]:
    # write your code here
    pass
