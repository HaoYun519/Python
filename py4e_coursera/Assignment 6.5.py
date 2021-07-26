str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find('de')
#print(float(atpos))
sppos = str.find('.',atpos)
#print(float(sppos)+42.0)


host = str[atpos:]
print(host)


