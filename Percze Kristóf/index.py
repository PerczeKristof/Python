from importlib import machinery
import math
from msvcrt import kbhit
from multiprocessing.sharedctypes import SynchronizedArray
from select import KQ_EV_ADD

"""
x= int (input ("Kérek egy egész számot"))
y= int (input ("Kérek egy egész számot"))

if x>0 and y>0:
    print("Első negyedben")
elif x>0 and y>0:
    print("Második negyedben")
elif x<0 and y<0:
    print("Harmadik negyedikben")
elif x==0 or y==0:
    print("A pont rajta van valamelyik tengelyen")
elif x==0 and y==0:
    print("A pont az origoban van")
else:
    print("Negyedik negyed") 

"""

"""
#Páros szám-e

c= int (input ("Kérek egy egész számot "))

if c%2 ==0:
    print("Páros szám")
else:
    print("Páratlan szám")
"""
# Írj egy programot amely beolva s egy n-et és egy m természetes számot, majd eldönti hogy n osztható-e m-el????

"""
n= int (input ("Kérek egy egész számot "))
m= int (input ("Kérek egy egész számot ")) 
 
if m!=0:
    if n%m==0:
        print("m osztója m-nek")
    else:
        print("Különben nem osztója")
else:
    print("nem adhatsz meg 0-t")
"""

#3.
"""
a= int (input("Kérek egy egész számot"))
b= int (input("Kérek egy egész számot"))
n= int (input("Kérek egy egész számot"))

if n>a and n<b:
    print("Beletartozik az intervallumba")
elif n<a or n>b:
    print(" Nem tartozik bele az intervallumba")
else:
    print("KEcske") """
"""
jegy= int (input("Kérek egy egész számot 1-5-ig"))

if jegy==1:
    print("elégtelen")
elif jegy==2:
        print("elégséges")
elif jegy==3:
        print("közepes")
elif jegy==4:
        print("jó")
elif jegy==5:
        print("jeles")
else:
    print("Joci") """

nap= str (input("Mondj egy napot"))

if nap=="Hétfő":
    print("Első nap")
elif nap=="Kedd":
    print("Második nap")
elif nap=="Szerda":
    print("Harmadik nap")
elif nap=="Csütörtök":
    print("Negyedik nap")
elif nap=="Péntek":
    print("Ötödik nap")
elif nap=="Szombat":
    print("Hatodik nap")
elif nap=="Vasárnap":
    print("Hetedik nap")
else:
    print("NEm jó")

    




