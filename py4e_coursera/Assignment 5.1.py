ct = 0
tot = 0
while True :
    nb = input('Enter number: ')
    if nb == 'done' :
        break
    try:
        nb = int(nb)
        #print(nb)
        ct = ct + 1
        tot = tot + nb
    except:
        print('Invalid input')
        continue
        
#print('ALL DONE')
print(tot,ct,float(tot/ct))