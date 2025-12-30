
basic = float(input("Enter basic salary: "))

DA = basic * 0.25
HRA = basic * 0.15
TA = basic * 0.075
PF = basic * 0.12

net_pay = basic + DA + HRA + TA
gross_pay = net_pay - PF

print("Net Pay:", net_pay)
print("Gross Pay:", gross_pay)
