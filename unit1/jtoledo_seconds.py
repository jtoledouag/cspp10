sec = int(input("enter a number of seconds"))
min = int(sec/60)
sec2 = sec%60
hrs = int(min/60)
min = min %60
print(hrs)
print(min)
print(sec2)
print(str(sec) + " seconds is " + str(hrs) + " hours,"+ str(min) + " minutes, and " + str(sec2) + " seconds. ")