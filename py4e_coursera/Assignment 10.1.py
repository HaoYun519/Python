fname = input('Enter the file name:  ')
fhand = open(fname)
email_addresses = {}

for line in fhand:
    if line.startswith('From ') : 
        email = line.split()[1]
        email_addresses[email] = email_addresses.get(email, 0) + 1
        # print(email_addresses[email])
# print(email_addresses)

lst=[]
for k,v in email_addresses.items():
    lst.append((v,k))

lst.sort(reverse=True)
person_tuple=lst[0]
print(person_tuple[1], person_tuple[0])