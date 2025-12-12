from random import *
import module1 #vaja panna siia kodid kuni "def lisamine" teisest failist ja panna siia
   
def vahetus(a,b): #vajab a,b
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n,loend,a,b):
    for i in range (n):#siin vaja sulk
        loend.append(randint(a,b))#siin vaja "." pärast loend ja ei vaja sulk

   

def jagamine(loend:list,p:list,n,nol):
    for el in loend:
        if el>0:
            p.append(el)#siin vaja "." pärast loend ja ei vaja sulk
        elif el<0: #siin vaja el<0:
            n.append(el)#siin vaja "." pärast loend ja ei vaja sulk
        else:
            nol.append(el)#siin vaja "." pärast loend ja ei vaja sulk

def keskmine(loend):
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    loend.append(el)#siin vaja "." pärast loend ja ei vaja sulk
    loend.sort()#siin vaja "." pärast loend ja ei vaja sulk
