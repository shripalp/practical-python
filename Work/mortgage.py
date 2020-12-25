#mortgage calculator
principal = float(input("principal:"))
rate = float(input("rate:"))
payment = float(input("payment:"))
total_paid = 0.0
while principal > 0:
    principal = principal * (1+rate/26) - payment
    total_paid = total_paid + payment
print('total paid:', total_paid)


 