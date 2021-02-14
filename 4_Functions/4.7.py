# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade 
# that takes a score as its parameter and returns a grade as a string.

def computegrade(score):
    if score >= 10.0:
        print("Bad score")
        exit()
    elif score >= 9.0:
        grade = "A"
    elif score >= 8.0:
        grade = "B"
    elif score >= 7.0:
        grade = "C"
    elif score >= 6.0:
        grade = "D"    
    else:
        grade = "F"        
    return(grade)

scoreInput = input("Enter score: ")

try: 
    scoreFlt = float(scoreInput)
    
except:
    print("Bad score")
    exit()

gradeResult = computegrade(scoreFlt)
print("Grade: ", gradeResult)
