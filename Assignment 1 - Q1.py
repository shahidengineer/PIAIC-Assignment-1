
# For Q1
print ("Q1 - Are female students performing better than male students in <given subject> (take user input).")

import Data4assignment as dfa 

# Defining a compare function    
def females_vs_males(subject_code):
    score_f = 0
    count_f = 0
    score_m = 0
    count_m = 0
    for a in dfa.data:
        if a [0] == "female":
            score_f += a[subject_code]
            count_f += 1
        else:
            score_m += a[subject_code]
            count_m += 1
    avg_score_f = score_f / count_f
    avg_score_m = score_m / count_m
    diff = avg_score_f - avg_score_m
    return diff

#Taking Input
while True:
    try:
        var_q1 = int (input ("\nEnter the code for subject (Maths = 1, Reading = 2, Writing = 3): "))
    except:
        print ("\nEnter a valid whole number... Try again!")
        continue
    if var_q1 >3 or var_q1 <0 or var_q1 == 0:
        print ("\nEnter a number between 1 to 3... Try again!")
        continue
    else:
        break

#Executing Input
sub_no = ("Maths","Reading","Writing") # Making a tuple for better printing of results
subject_code = var_q1 + 2
diff = females_vs_males(subject_code)
if diff > 0:
    print (f"\nAns-2: Yes, average score of Females in subject {sub_no[var_q1-1]} is better than Males.")
elif diff == 0:
    print (f"\nAns-2: No, average score of Females in subject {sub_no[var_q1-1]} are as good as Males")
else:
    print (f"\nAns-2: No, average score of Males in subject {sub_no[var_q1-1]} is better than Females.")
