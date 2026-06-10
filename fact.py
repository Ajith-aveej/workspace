"""def fat(num):
    factorial =1
    for i in range (1,num+1,1):
        factorial *=i
    return factorial
numb = int(input("enter the values to get factorial of that \t"))
print(fat(numb)) """

"""   
stri = input("enter any string for validation\n")
def count_stri(stri):
    dect = {}
    repeat =0
    for item in stri:
        repeat=stri.count(item)
        dect[item] = repeat
        #print(f"{stri} has {item} found {repeat} times in given string" )
    print(dect)
count_stri(stri)
     """
a = input()
b = input()
count =0
for j in range (len(a)) :
    for i in range(len(b)):
        if a[j] == b[i]:
            count +=1
if count == len(a):
    print("strings are anagrams")
    
else:
    
    print("not anagrams")
            
     
    
    

        

