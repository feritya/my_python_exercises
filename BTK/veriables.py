payment_joey      =2550
payment_lilly       =3500
tax                       =0.21
overtime_wage    =22
joey_overtime      =52
lilii_overtime        =25

print("\njoey made: ",payment_joey-( payment_joey*tax), "$ this month")
print("lilly made: ",payment_lilly-( payment_lilly*tax), "$ this month\n")

joey_total=(payment_joey-( payment_joey*tax))+(overtime_wage*joey_overtime)
lilly_total =(payment_lilly-( payment_lilly*tax))+(overtime_wage*lilii_overtime)

print("Joey receives ",joey_total," $ with overtime pay")
print("lilly receives ",lilly_total," $ with overtime pay\n")
