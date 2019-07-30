n11=int(input())
a1=1
b1=1
for i in range(0,n11):
  if i!=n11-1:
    print(a1,end=" ")
  else:
    print(a1)
  c1=a1+b1
  a1=b1
  b1=c1
