#program to convert time into corresponding hour,minute and second
#input time in seconds
second=int(input("Enter the time in seconds:"))
#check second is negative or not
if second<0:
    exit("Time cannot be negative")
#-------------------------------------------------------
print("-----------")
hour=0
minute=0
#converting number of seconds into hours
if second>=3600:
    hour=second//3600
    second=second%3600
#---------------
#converting number of seconds into minutes
if second>=60:
    minute=second//60
    second=second%60
#----------------------------------------
print(hour,"hours",minute,"minutes",second,"seconds")
