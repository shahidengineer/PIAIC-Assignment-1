print ("Q6 - How many parents have bachelors education, master education, or some college degrees level education?")
print ()
import Data4assignment as dfa
count_m = 0
count_b = 0
count_sc = 0
for a in dfa.data:
    if a[1] == "bachelor's degree":
        count_b += 1
    elif a[1] == "master's degree":
        count_m += 1
    elif a[1] == "some college":
        count_sc += 1
total_count = count_b + count_m + count_sc
print ("ANS - 6")
print (f"The total no of parents with master\'s degree = {count_m}")
print (f"The total no of parents with backelors\'s degree = {count_b}")
print (f"The total no of parents with some college degree = {count_sc}")
print (f"The total no. of parents with either Masters's, Bachelor's or some College Degree = {total_count}")