principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = int(input('start month:'))
extra_payment_end_month = int(input('end month:'))
extra_payment = float(input('extra payment:'))

while principal > 0:
    while months > (extra_payment_start_month -2) and months < (extra_payment_end_month) :
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
        months = months + 1
        print(months, round(total_paid, 2), round(principal, 2))
        
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months + 1
    print(months, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('months', months)