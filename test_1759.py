# Test Case 1: Basic test case with n = 2 and m = 4
# The input list is ['a', 'b', 'c', 'd']
# The combinations of length 2 are [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
# The combinations of length 2 without vowels are [('b', 'c'), ('b', 'd'), ('c', 'd')]
# The output should be 'ab'
assert your_function_name(2, 4, ['a', 'b', 'c', 'd']) == 'ab'

# Test Case 2: Basic test case with n = 3 and m = 5
# The input list is ['a', 'b', 'c', 'd', 'e']
# The combinations of length 3 are [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'b', 'e'), ('a', 'c', 'd'), ('a', 'c', 'e'), ('a', 'd', 'e'), ('b', 'c', 'd'), ('b', 'c', 'e'), ('b', 'd', 'e'), ('c', 'd', 'e')]
# The combinations of length 3 without vowels are [('b', 'c', 'd'), ('b', 'c', 'e'), ('b', 'd', 'e'), ('c', 'd', 'e')]
# The output should be 'abc'
assert your_function_name(3, 5, ['a', 'b', 'c', 'd', 'e']) == 'abc'

# Test Case 3: Test case with n = 1 and m = 3
# The input list is ['a', 'b', 'c']
# The combinations of length 1 are [('a',), ('b',), ('c',)]
# The combinations of length 1 without vowels are [('b',), ('c',)]
# The output should be 'b'
assert your_function_name(1, 3, ['a', 'b', 'c']) == 'b'