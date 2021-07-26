hrs = input('Enter Hours?:')
rate = input('Enter rate?:')

while True :
 try:
    hrs = float(hrs)
    rate= float(rate)
    if hrs > 40:
        pay = (40*rate) + ((hrs-40)*(rate*1.5))
    else :
        pay = hrs * rate
    print(pay)
    
 except:
    print('Error, please enter numeric input')