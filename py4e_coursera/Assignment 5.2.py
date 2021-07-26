num = 0
largest = 0
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        numb = int(num)
    except:
        print("Invalid input")
    if smallest is None:
        smallest = numb  #賦予Smallest value 只跑一次
    elif numb < smallest:
        smallest = numb
    elif numb > largest:
        largest = numb


print("Maximum is", largest)
print("Minimum is", smallest)