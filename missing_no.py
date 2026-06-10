lis = [1,2,3,5,6,7]
i =1
while i < len(lis):
    item =lis[i-1]
    if lis[i]-item ==2:
        print(f"number {lis[i]-1} is missing in a list")
        break
    else:
        i=i+1
        