taxrate = 0
kid = bool(input("Any kids > "))
salaryK = float(input("What's  your salary > "))
if (30 < salaryK <= 50):
    taxrate = 35 if kid else 40
elif (50 < salaryK <= 70):
    taxrate = 45 if kid else 50
else:
    taxrate = 55 if (salaryK >= 70) else 0

print(taxrate)