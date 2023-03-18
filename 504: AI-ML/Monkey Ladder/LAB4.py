# TC1_LAB4
# SIA VASHIST_ 20190802107
# Monkey Ladder Problem
"""
def climbStairs(N):
    if N <= 2:
        return 1
    else:
        return climbStairs(N - 1) + climbStairs(N - 2)


steps = int(input("Enter the number of steps: "))
ways = climbStairs(steps)
print("There are " + str(ways) + " distinct ways to climb a staircase of " + str(
    steps) + " steps when climbing up one or two steps at a time.")
"""


def Climber(n, knownWays={}):
    if n in knownWays:
        return knownWays[n]
    if n == 0 or n == 1:
        return 1
    else:
        knownWays[n] = Climber(n - 1, knownWays) + Climber(n - 2, knownWays)
        return knownWays[n]

steps = int(input("Enter the number of steps: "))
ways = Climber(steps)
print("There are " + str(ways) + " distinct ways to climb a staircase of " + str(
    steps) + " steps when climbing up one or two steps at a time.")


