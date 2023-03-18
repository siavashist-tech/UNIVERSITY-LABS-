# TC1_LAB3
# SIA VASHIST_ 20190802107
# Water Jug Problem

from collections import defaultdict

# Initialize dictionary with default value as false.
visited = defaultdict(lambda: False)

# jug1 and jug2 contain the value for max capacity in respective jugs
# and Target is the amount of water to be measured.
# To store J1, J2 and Target
J1, J2, Target = 0, 0, 0


def WaterJugSolver(X, Y):
    global J1, J2, Target

    # Checks for our goal and
    # returns true if achieved.
    if (X == Target and Y == 0) or (Y == Target and X == 0):
        print("(", X, ", ", Y, ")", sep="")
        return True

    # Checks if the state is already visited
    # If not, then it proceeds further.
    if not visited[(X, Y)]:
        print("(", X, ", ", Y, ")", sep="")

        # Marking the current state as visited
        visited[(X, Y)] = True

        return (WaterJugSolver(0, Y) or
                WaterJugSolver(X, 0) or
                WaterJugSolver(J1, Y) or
                WaterJugSolver(X, J2) or
                WaterJugSolver(X + min(Y, (J1 - X)),
                               Y - min(Y, (J1 - X))) or
                WaterJugSolver(X - min(X, (J2 - Y)),
                               Y + min(X, (J2 - Y))))

    else:
        return False


# Main Code

J1 = int(input("Enter the Capacity of Jug1: "))
J2 = int(input("Enter the Capacity of Jug2: "))
Target = int(input("Amount to be measured: "))

print("Path is as Follow:")

WaterJugSolver(0, 0)
