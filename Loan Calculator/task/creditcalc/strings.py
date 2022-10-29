years = number_of_months // 12
        months = number_of_months % 12
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
