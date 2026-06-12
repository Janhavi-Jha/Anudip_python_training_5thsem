'''screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]
Tasks
1. Calculate average screen time.
2. Find the highest and lowest screen time.
3. Count days exceeding 200 minutes.
4. Display days with healthy usage (<180 minutes).
5. Categorize usage:
o Healthy (<180)
o Moderate (180–240)
o Excessive (>240) '''
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]
#calculate average screen time
total=0
for i in screen_time:
    total+=i
average=total/len(screen_time)
print("Average=",average)
#highest screen time
highest=0 
for i in screen_time:
    if i>highest:
        highest=i
print("Highest screen time=",highest)
#lowest screen time
lowest=180
for i in screen_time:
    if i <lowest:
        lowest=i
print("Lowest screen time=",lowest)
#count days exceeding 200 days
count=0
for i in screen_time:
    if i>200:
        count+=1
print("Days exceeding 200 minutes:",count)
#Display days with healthy usage (<180 minutes)
print("Days with healthy usage (<180 minutes):")
day = 1

for i in screen_time:
    if i < 180:
        print("Day", day)
    day += 1
#categorize usage 
healthy=0
moderate=0
excessive=0
for i in screen_time:
    if i<180:
        healthy+=1
    elif i>=180 and i<=240:
        moderate+=1
    else:
        excessive+=1
print("Healthy=",healthy)
print("Moderate=",moderate)
print("Excessive=",excessive)
