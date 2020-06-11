print ("Q8 - How many students have good in reading (> 75) but not good in writing( < 70)")
import Data4assignment as dfa
count_rw = 0
for a in dfa.data:
    if a[4] > 75 and a[5] < 70:
        count_rw += 1
print ("\nANS-8:\n")
print (f"The total no of students with good reading (>75) and not good writing (<70) scores is {count_rw}.")