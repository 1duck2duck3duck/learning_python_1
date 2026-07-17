def invest(amount, rate, years):
    for year in range(1, years + 1)
        amount *= (1 + rate/100)
        print(f"Year {n}: ${amount:.2f}")


amount = float(input("Please enter amount start:  "))
years  = int(input("Please enter years:  "))
rate = float(input("Please enter your procent(%)"))

invest(amount, rate, years)

