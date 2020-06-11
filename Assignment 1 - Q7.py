print ("Q7 - In a user given subject score, is the top scorer a female or male?") 
print ()
import Data4assignment as dfa

#Defining Function
def female_vs_male_score (user_input_subject):
    count_f = 0
    score_f = 0
    count_m = 0
    score_m = 0
    user_input_sub = user_input_subject + 2
    for a in dfa.data:
        if a[0] == "female":
            score_f = score_f +  a[user_input_sub]
            count_f += 1
        else:
            score_m = score_m + a[user_input_sub]
            count_m += 1
    avg_score_f = score_f / count_f
    avg_score_m = score_m / count_m
    diff = avg_score_f - avg_score_m
    return diff 

#Taking and executing input
user_input_subject = int (input ("Please enter the code of the subject score you like to check (1: Maths, 2: Reading, 3: Writing): "))
subejct_list = ("Maths", "Reading", "Writing")
print ("\nANS - 7:\n")
diff = female_vs_male_score (user_input_subject)
if user_input_subject < 3 and user_input_subject > 0:
    if diff > 0:
        print (f"Females are Top Scorer in {subejct_list[user_input_subject-1]}.")
    elif diff == 0:
        print (f"The Females scored equal to Males in {subejct_list[user_input_subject-1]}.")
    else:
        print (f"No, the Males are Top Scorer in {subejct_list[user_input_subject-1]}.")
else:
    print ("Invalid Input !!")