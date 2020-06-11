# For Q3
print ("\nQ3- what is the impact of parent education in student performance good, bad, or no impact?")

import Data4assignment as dfa

# Making a list of parent's eduction in asecending order
parent_edu = ["high school",
              "some high school", 
              "some college", 
              "associate's degree", 
              "bachelor's degree", 
              "master's degree"]

total_score_list = []
for a in parent_edu:
    count = 0
    total_score = 0
    for b in dfa.data:
        if b[1] == a:
            total = b[3]+b[4]+b[5]
            count += 1
            total_score += total
    avg_total = round(total_score/count,2)
    total_score_list.append(avg_total)
if total_score_list == sorted (total_score_list):
    print ("\nAns-3: The parents education has Good Impact on student scores.")
elif total_score_list == sorted (total_score_list, reverse=True):
    print ("\nAns-3: The parents education has Bad Impact on student scores.")
else:
    print ("\nAns-3: The parents education has NO Impact on student scores.")
print ("\n01 Observation in Data : Some high school education is placed higher than high school education in list")
print ("to make get the propoer order or the data in each category must be interchanged to get the better answer.")