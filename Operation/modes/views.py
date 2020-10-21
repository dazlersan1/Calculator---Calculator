from django.shortcuts import render
from django.contrib import messages
def extended(a,b):
  if(b==0):
    return a,1,0
  else:
    d,p,q=extended(b,a%b)
    x=q
    y=p-q*(a//b)
  return d,x,y
    

def gcd(a, b):
  

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)

def diophantine(a, b, c):
  assert c % gcd(a, b) == 0
  g=gcd(a,b)
  ans=c//g
  rep,x,y=extended(a,b)
  
  return (x*ans, y*ans)

print(diophantine(4,13,13))
def inv(request):
    if(request.method=='POST'):
        a=int(request.POST['a'])
        mod=int(request.POST['mod'])
        if(gcd(a,mod)!=1):
            messages.info(request,"Inverse doesn't exist")
        else:
            ans,b=diophantine(a,mod,1)
            messages.info(request,"The inverse of "+str(a)+ " mod " + str(mod)+" is "+str(ans%mod))
        return render(request,'index.html')
        
        
    return render(request,'index.html')
