#Check palindrome: O(n^2) Vs O(n)

def method_1_O_n2(inputString):
    flag=1
    for i in range(0,len(inputString)):
        for j in range(len(inputString)-1,0,-1):
            if inputString[i]==inputString[j]:
                pass
            else:
                flag=0
    if(flag==1):
        print("it's a Palindrome")
    else:
        print("Nope")

def method_2_O_n(inputString):
    if(inputString==inputString[::-1]):
        print("it's a Palindrome")
    else:
        print("Nope")
    
inputString=input("write down the string: ")
method_1_O_n2(inputString)
method_2_O_n(inputString)
