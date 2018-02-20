def ps23(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate / 12.0

    low = balance / 12.0
    high = (balance * (1 + monthlyInterestRate)**12) / 12.0
    ans = (high + low) / 2.0

    monthlyUnpaidBalance = balance - ans
    newMonthlyBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

    def bi23(balance, annualInterestRate,low,high):

        ans = (high + low) / 2.0
        epsilon = 0.1

        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - ans
        newMonthlyBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

        while abs(newMonthlyBalance) - 1 > epsilon:
            for m in range(1,12):
                monthlyInterestRate = annualInterestRate / 12.0
                monthlyUnpaidBalance = newMonthlyBalance - ans
                newMonthlyBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            if abs(newMonthlyBalance) - 1 < epsilon:
                break
            elif newMonthlyBalance > 0:
                low = ans
                return bi23(balance,annualInterestRate,low,high)
            else:
                high = ans
                return bi23(balance,annualInterestRate,low,high)
            ans = (high + low) / 2.0
        return round(ans,2)
    return "Lowest Payment: ", bi23(balance,annualInterestRate,balance/12.0,(balance * (1 + monthlyInterestRate)**12) / 12.0)
	print(ps23(balance,annualInterestRate))