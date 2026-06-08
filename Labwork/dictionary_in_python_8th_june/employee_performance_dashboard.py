'''Employee performance scores are stored as: performance = {     "EMP101": 92,     "EMP102": 78,     "EMP103": 45,     "EMP104": 88,     "EMP105": 97,     "EMP106": 56,     "EMP107": 81,     "EMP108": 64,     "EMP109": 39,     "EMP110": 73 } Tasks 1. Display employees scoring above 80.  2. Count employees needing improvement (score < 60).  3. Find the top performer.  4. Calculate average performance score. '''
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Employees scoring above 80
print("Employees scoring above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp, score)

# 2. Employees needing improvement (<60)
print("\nEmployees needing improvement:")
for emp, score in performance.items():
    if score < 60:
        print(emp, score)

# 3. Top performer
top_emp = ""
top_score = 0# to ensure any real score is bigger 

for emp, score in performance.items():
    if score > top_score:
        top_score = score
        top_emp = emp

print("\nTop performer:", top_emp, top_score)

# 4. Average score
total = 0
for score in performance.values():
    total += score

average = total / len(performance)
print("\nAverage score:", average)

# 5. Categorization
excellent = []
good = []
avg = []
poor = []

for emp, score in performance.items():
    if score >= 90:
        excellent.append((emp, score))
    elif 75 <= score <= 89:
        good.append((emp, score))
    elif 60 <= score <= 74:
        avg.append((emp, score))
    else:
        poor.append((emp, score))

print("\nExcellent:", excellent)
print("Good:", good)
print("Average:", avg)
print("Poor:", poor)
