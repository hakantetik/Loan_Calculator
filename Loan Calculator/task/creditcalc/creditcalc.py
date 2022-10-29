import math
import argparse

parser = argparse.ArgumentParser(description="This program is a credit calculator.")
parser.add_argument("--type", choices=["annuity", "diff"], help="Incorrect parameters", required=True)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)

args = parser.parse_args()
calculations = [args.type, args.principal, args.periods, args.interest, args.payment]

if calculations.count(None) > 1:
    print("Incorrect parameters.")
elif args.type not in ("diff", "annuity"):
    print("Incorrect parameters")
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")

elif args.type == "annuity" and args.principal is None:
    i = args.interest / 1200
    n = args.periods
    payment = args.payment

    body = math.pow(1 + i, n)

    loan_principal = math.floor(payment / (i * body / (body - 1)))
    total = payment * n
    overpayment = total - loan_principal

    print(f"""
    Your loan principal = {loan_principal}!
    Overpayment = {overpayment}
    """)
elif args.type == "annuity" and args.payment is None:
    i = args.interest / 1200
    n = args.periods
    loan_principal = args.principal
    body = math.pow(1 + i, n)
    annuity_payment = math.ceil(loan_principal * (i * body / (body - 1)))

    total = annuity_payment * n
    overpayment = math.floor(total - loan_principal)

    print(f"""
    Your annuity payment = {annuity_payment}!
    Overpayment = {overpayment}
    """)
elif args.type == "annuity" and args.periods is None:
    i = args.interest / 1200
    principal = args.principal
    payment = args.payment
    body = float(payment / (payment - i * principal))
    number_of_months = math.ceil(math.log(body, 1 + i))
    print("number of months", number_of_months)

    years = number_of_months // 12
    print("years", years)
    months = number_of_months % 12
    print("months", months)
    if number_of_months % 12 == 0 and years == 1:
        print(f"It will take {years} year to repay this loan!")
    elif number_of_months % 12 == 0 and years > 1:
        print(f"It will take {years} years to repay this loan!")
    elif number_of_months % 12 > 0:
        if years == 1 and months == 1:
            print(f"It will take {years} year and {months} to repay this loan!")
        elif years == 1 and months > 1:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif years > 1 and months == 1:
            print(f"It will take {years} years and {months} month to repay this loan!")
        elif years > 1 and months > 1:
            print(f"It will take {years} years and {months} months to repay this loan!")

    overpayment = payment * number_of_months - principal
    print(f"Overpayment 0 {overpayment}")
elif args.type == "diff" and args.payment is None:
    i = float(args.interest / 1200)
    n = args.periods
    principal = args.principal
    total = 0
    for m in range(1, n + 1):
        payment = math.ceil(principal / n + i * (principal - (principal * (m - 1) / n)))
        print(f"Month {m}: payment is {payment}")
        total += payment

    overpayment = total - principal
    print(f"Overpayment = {overpayment}")
