score = input("Enter score: ")

try: 
    scoreFlt = float(score)
except:
    print("Bad score")
    exit()

if scoreFlt >= 10.0:
    print("Bad score")
elif scoreFlt >= 9.0:
    print("Grade: A")
elif scoreFlt >= 8.0:
    print("Grade: B")
elif scoreFlt >= 7.0:
    print("Grade: C")
elif scoreFlt >= 6.0:
    print("Grade: D")
else:
    print("Grade: F")
