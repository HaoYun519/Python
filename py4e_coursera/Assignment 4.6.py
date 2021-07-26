def computepay(hrs, rate):
    print('In computepay', hrs, rate)

hrs = input('Enter Hours?:')
rate = input('Enter rate?:')
hrs = float(hrs)
rate= float(rate)

if hrs > 40 and rate > 0:
    computepay(hrs, rate)
    pay = (40*rate) + ((hrs-40)*(rate*1.5))
    print(pay)
elif 40 >= hrs >= 0 and rate > 0:
    computepay(hrs, rate)
    pay = hrs * rate
    print(pay)
else:
    print('Error, please enter vaild number')