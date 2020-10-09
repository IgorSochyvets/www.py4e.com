# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, 
# and print out the converted temperature.
# (0 °C × 9/5) + 32 = 32 °F
# °F = °C * 1.8 + 32.00



celsius = input("Enter Celsius Temperature: ")

fahrenheit =  ( float(celsius) * 9/5) + 32

print("Temperature in Fahrenheit: ",fahrenheit)