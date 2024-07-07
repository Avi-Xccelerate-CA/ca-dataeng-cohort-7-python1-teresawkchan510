# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE

    prescription = []

    if sum(needs) < 500:
        for n in needs:
             vitamin = 0
             injection = 0

             if n > 250:
                 return "No medicine given"
             elif n%10 == 0:
                vitamin = n//10
                injection = 0
                prescription.append((vitamin, injection))
             else:
                vitamin = n//10 + 1
                injection = 10 - n%10
                prescription.append((vitamin, injection))

        return prescription
    else:
        return "No medicine given"

    #YOUR SOLUTION ENDS HERE