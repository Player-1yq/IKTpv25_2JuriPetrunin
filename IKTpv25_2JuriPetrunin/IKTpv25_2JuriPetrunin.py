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
