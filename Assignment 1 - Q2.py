# For Q2
print ("Q2- Are students that have done preparation courses are good in courses or not.")

import Data4assignment as dfa 

# Defining a function
def completed_vs_none ():
    score_c = 0
    count_c = 0
    score_n = 0
    count_n = 0
    for a in dfa.data:
        if a[2] == "completed":
            score_c = score_c + a[3] + a[4] + a[5]
            count_c += 1
        else:
            score_n = score_n + a[3] + a[4] + a[5]
            count_n += 1
    avg_score_c = score_c / count_c
    avg_score_n = score_n / count_n
    diff = avg_score_c - avg_score_n
    return diff

# Running code for the answer
diff = completed_vs_none()
if diff > 0 :
    print ("\nAns-2: The students with preparation courses \"completed\" are good in courses.")
elif diff == 0:
    print ("\nAns-2: The students with preparation courses \"completed\" are as good in courses as other students with no preparation courses.")
else:
    print ("\nAns-2: The students with preparation courses \"completed\" are not good in courses.")