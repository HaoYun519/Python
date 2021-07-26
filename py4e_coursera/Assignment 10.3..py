alphabet = 'abcdefghijklmnopqrstuvwxyz'

filename=input("Enter a file name: ")
fhand = open(filename,'r')
text = fhand.read()


freq_dict = {}
for ch in text.lower():
    if ch in alphabet:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1

lst=[]
for k,v in freq_dict.items():
    lst.append((v,k))

lst.sort(reverse=True)

for letter, freq in lst:
    print(freq, letter)