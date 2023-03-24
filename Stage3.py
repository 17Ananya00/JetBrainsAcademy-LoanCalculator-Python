import math
print("What do you want to calculate?" + "\n" +
      ' type "n" for number of monthly payments,' + '\n' +
      'type "a" for annuity monthly payment amount,' + '\n' +
      'type "p" for loan principal:')
calc = input();

if calc == "n":
    P = float(input("Enter the loan principal:\n"))
    A = float(input("Enter the monthly payment:\n"))
    i = float(input("Enter the loan interest:\n")) / (12 * 100)
    n = math.ceil(math.log(A / (A - i * P), 1 + i))
    year = n // 12
    month = n % 12
    if n % 12 != 0:
        print("It will take " + str(year) + " years and " + str(month) + " months to repay this loan!")
    elif n % 12 == 0:
        print("It will take " + str(year) + " years to repay this loan!")
    elif n // 12 == 0:
        print("It will take " + str(month) + " months to repay this loan!")
elif calc == "a":
    P = float(input("Enter the loan principal:\n"))
    n = float(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n")) / (12 * 100)
    A = math.ceil(P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print("Your monthly payment = " + str(A) + "!")
elif calc == "p":
    A = float(input("Enter the annuity payment:\n"))
    n = float(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n")) / (12 * 100)
    P = round(A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print("Your loan principal = " + str(P) + "!")
