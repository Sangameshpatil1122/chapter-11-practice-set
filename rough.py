pos=neg=zero=0
print("Enter numbers one by one. Type 'a' to finish.")
while True:
    num_str= input("Enter a number or (a to stop): ")
    if num_str=='a':
        break
    num=int(num_str)
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        zero+=1

print("Positive numbers:", pos)
print("Negative numbers:", neg) 
print("Zeros:", zero)
