print ("Q4: Is there any difference in student score if parents have master-level education in a specified score")
print ("Q5: Is there any difference in student score if parents have Bachler level education in a specified score")
print ("This is a combo program for any combination of parents enducation and subject list")
print ()
import Data4assignment as dfa
parents_edu_list = ["high school",
            "some high school", 
            "some college", 
            "associate's degree", 
            "bachelor's degree", 
            "master's degree"]
sub_no = ("Maths","Reading","Writing")
def parents_edu (user_input_parent, user_input_subject):
    b = user_input_parent - 1
    user_input_parent_str = parents_edu_list [b]
    user_input_subject = user_input_subject + 2 # Indexing the subject
    count_user = 0
    total_score_user = 0
    count_bal = 0
    total_score_bal = 0
    for a in dfa.data:
        if a[1] == user_input_parent_str:
            total_score_user += a[user_input_subject]
            count_user += 1
        else:
            total_score_bal += a[user_input_subject]
            count_bal += 1
    avg_score_user = round (total_score_user / count_user, 2)
    avg_score_bal = round (total_score_bal / count_bal, 2)
    diff = avg_score_user - avg_score_bal
    return diff

user_input_parent = int (input("""Please enter the code for Parent's Degree - 
1: High School
2: Some High School
3: Associate's Degree
4: Bachelor's Degree
5: Master's Degree
"""))
user_input_subject = int (input ("""Please enter the code for subject -
1: Maths
2: Reading 
3: Writing
"""))
print ()
if user_input_parent < 6 and user_input_parent > 0 and user_input_subject > 0 and user_input_subject < 3:
    if parents_edu (user_input_parent, user_input_subject) > 0:
        print (f"The students with parent's eduction \"{parents_edu_list[user_input_parent-1].title()}\", scored high in subject \"{sub_no[user_input_subject-1]}\" compared to others.")
    elif parents_edu (user_input_parent, user_input_subject) == 0:
        print (f"The students with parent's eduction \"{parents_edu_list[user_input_parent-1].title()}\", scored similar to others in subject \"{sub_no[user_input_subject-1]}\".")
    else:
        print (f"The students with parent's eduction \"{parents_edu_list[user_input_parent-1].title()}\", scored low in subject \"{sub_no[user_input_subject-1]}\" compared to others.")
else:
    print ("Invalid Input!!")