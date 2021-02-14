# Exercise 2: Write another program that prompts for a list of numbers as above and at 
#the end prints out both the maximum and minimum of the numbers instead of the average.

list = []

max = None
count = 0
min = None

print("Input numbers and finish with 'done':")

while True:
    try:
        line = input('> ')
        if line == 'done':
            break
        list.append(int(line))
        if max is None:
            max = list[count] 
        else:
            if list[count] > max:
                max = list[count]

        if min is None:
            min = list[count]
        else:
            if list[count] < min:
                min = list[count]

        count = count + 1    
        print("Max is: ", max, "Min is: ", min)
    except:
        print("Error, put a number")
print("Maximum number is: ", max, "Minimum number is: ", min)
