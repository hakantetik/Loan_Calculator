annuity_payment = float(input("Enter the annuity payment:"))
number_of_payments = int(input("Enter the number of periods:"))
loan_interest = float(input("Enter the loan interest:"))

i = float(loan_interest / (12 * 100))
body = math.pow(1 + i, number_of_payments)

loan_principal = math.floor(annuity_payment / ((i * body) / (body - 1)))
print(f"Your loan principal = {loan_principal}!")


if response == "a":
    loan_principal = int(input("Enter the loan principal:"))
    number_of_months = int(input("Enter the number of periods:"))
    loan_interest = float(input("Enter the loan interest:"))

    i = float(loan_interest / (12 * 100))
    body = math.pow(1 + i, number_of_months)
    monthly_payment = math.ceil(loan_principal * ((body * i) / (body - 1)))

    print(f"Your monthly payment = {monthly_payment}")
