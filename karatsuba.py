#karatsuba mul

def karatsuba (num1,num2):

    #base case
    if (len(num1)==1 or len(num2)==1):
        return str(int(num1)*int(num2))
    
    max_len = max(len(num1),len(num2))
    if max_len % 2 != 0:
        max_len += 1
    num1=num1.zfill(max_len)
    num2=num2.zfill(max_len)

    m=max_len//2

    a,b = num1[:-m],num1[-m:]
    c,d = num2[:-m],num2[-m:]
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    adplusbc=karatsuba(str(int(a)+int(b)),str(int(c)+int(d)))

    product = int(ac)*10**(2*m)+(int(adplusbc)-int(ac)-int(bd))*10**m+int(bd)

    return str(product)

print(karatsuba("1234","124"))