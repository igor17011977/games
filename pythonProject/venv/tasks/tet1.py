from decimal import *
n = int(input())
a=[]

for y in range(n*2,n,-1):

#    x =Decimal(1 / (Decimal(1 / n) - Decimal(1 / y)))
    x=Decimal((y*n)/(y-n))
#    print(x,Decimal(1 / y))
#    x=x.quantize(Decimal("1.00"))
#    x=round(x,4)
    if Decimal(x) % 1==0:
 #       print(f"1/{n} = 1/{x} + 1/{y}")
        a.append([int(x), int(y)])
a.sort(reverse = True)
for t in a:
     print(f"1/{n} = 1/{t[0]} + 1/{t[1]}")
