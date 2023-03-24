import math

print("Enter the loan principal:");
principal = float(input());
print("What do you want to calculate?" + "\n" +
      'type "m" - for number of monthly payments,' + '\n' +
      'type "p" - for the monthly payment:');
calc = input();

if calc == "m":
    monthly_payment = float(input("Enter the monthly payment:"));
    number_of_months = math.ceil(principal/monthly_payment);
    if number_of_months == 1:
        print("It will take 1 month to repay the loan");
    else:
        print("It will take " + str(number_of_months) + " months to repay the loan");

elif calc == "p":
    print("Enter number of months:")
    months = int(input())
    if (months % 2) == 0:
        payment = int(round(principal // months))
        print("Your monthly payment = " + str(payment))
    else:
        payment = int(round(principal // months)) + 1
        last_payment = principal - (months - 1) * payment
        print("Your monthly payment = " + str(payment) + " and the last payment = " + str(last_payment))


