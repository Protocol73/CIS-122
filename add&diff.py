#add&diff.py -Protocol73

number1 = raw_input("Input a Number:")
number2 = raw_input("Put in another Number:")

added = int(number1) + int(number2)
diff = int(number1) - int(number2)

diff_absolute = abs(diff)

print ("Your Numbers added are:") + (str(added))
print ("The Difference is:") + (str(diff_absolute))