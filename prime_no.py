limit = int(input("enter the limit to generate prime number\t"))
if limit in (0,1):
    print("no prime number found in this limit")
elif limit == 2:
    print("one prime number is found that is 2")
elif limit == 3:
    print("found two prime number within this value:\n2\n3")
else:
    print(f"{2}\n{3}\n{5}\n{7}")
    for prime in range (4,limit):
        if not prime%2==0 and not prime%3==0 and not prime%5 ==0 and not prime%7==0:
            print(prime)
    
    