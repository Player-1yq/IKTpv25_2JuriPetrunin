from random import *
import module1 #teha module ja kooperita kodid kuni "def lisamine"

   
def vahetus(a,b): #vajab a,b
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n,loend,a,b): #lisab loendisse n juhuslikku arvu vahemikust a kuni b
    for i in range (n):#siin vaja sulk
        loend.append(randint(a,b))#siin vaja "." pärast loend ja ei vaja sulk

   

def jagamine(loend:list,p:list,n,nol):#jagab loendi elemendid positiivseteks (p), negatiivseteks (n) ja nullideks
    for el in loend:
        if el>0:
            p.append(el) #siin vaja "." pärast loend ja ei vaja sulk
        elif el<0: #siin vaja el<0:
            n.append(el) #siin vaja "." pärast loend ja ei vaja sulk
        else:
            nol.append(el) #siin vaja "." pärast loend ja ei vaja sulk

def keskmine(loend): #leiab loendi elementide keskmise.
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
    loend.append(el) #siin vaja "." pärast loend ja ei vaja sulk
    loend.sort() #siin vaja "." pärast loend ja ei vaja sulk










             



from random import *
from module1 import*


#Põhifunktsioon
def arvud_loendis():
        """Kirjandus

        Küsib, kui palju arve genereerida.
        Küsib juhuarvude vahemiku.
        Genereerib juhuslike täisarvude loendi.
        Sorteerib selle täisarvu.
        Jagab loendi kolmeks: positiivsed, negatiivsed ja nullid.
        Leiab positiivsete ja negatiivsete keskmised.
        Lisab need keskmised algsesse loendisse.
        Sorteerib ja väljastab lõpliku loendi.
    """
print("Andmed:")
n=abs(int(input("Mitu täisarvu genereerime loendisse? => ")))
mini=int(input("Sisesta vahemiku minimaalne arv => "))
maxi=int(input("Sisesta vahemiku maksimaalne arv => "))
if mini>=maxi:
    mini,maxi =vahetus(mini,maxi)

    #kustuda ":" kus nad olid
    s=[]#Alghe loend
    pos=[]#positiivse
    neg=[]
    null=[]
    generaator(n,s,mini,maxi)#tabulatsioon
    print()
    print("Tulemused:")
    print("Saadud loend alates",mini,"kuni",maxi,s)
    s.sort() #s.sort
    print("Sorteeritud loend",s)# siin vaja ,
    jagamine(s,pos,neg,null)
    print("Positiivsete elementide loend",pos)
    print("Negatiivsete elementide loend",neg)
    print("Null-elementide loend",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Positiivsete keskmine:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Negatiivsete keskmine:",kesk)
    print("Lisame keskmised algsesse massiivi:")
    s.sort() # s.sort
    print(s)
   


#Põhifunktsiooni käivitus
arvud_loendis()
