"""
This code just tells you, if there are any two values in both lists, that add up to v !
And not which numbers exactly !
"""

a = [0, 0, -5, 8, -10, 1013, -100, 1]
b = [-10, 40, -3, 9, 8, 0, -5]
v = -15


summand = any([v-i in b for i in a])
print(summand)
