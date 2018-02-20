def pset22(balance, annualInterestRate, month):
	def ps(balance, annualInterestRate, MMP):
		MIR = annualInterestRate/12.0
		MUB = balance - MMP
		UMB = MUB + (MIR * MUB)
		for m in range(1,month):
			MIR = annualInterestRate / 12.0
			MUB = UMB - MMP
			UMB = MUB + (MIR * MUB)
		if UMB < 0:
			return MMP
			print("Lowest Payment: " + MMP)
		else:
			return ps(balance, annualInterestRate, MMP+10)
	print("Lowest Payment: ", ps(balance, annualInterestRate,0))
	return "Lowest Payment: ",ps(balance, annualInterestRate, 0)
balance1 = input("enter balance: ")
annualInterestRate1 = input("enter annual interest rate: ")
month1 = input("enter in how many months you wish to pay off balance: ")
print(pset22(float(balance1),float(annualInterestRate1),int(month1)))