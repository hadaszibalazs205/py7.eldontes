#Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!

import random

lista = []

for i in range(5):
  lista.append(random.randint(1, 7))
  
szam = int(input("Adj meg egy számot: "))

if szam in lista:
  print("Ez a szám megtalálható a listában")
else:
  print("Ez a szám nem található meg a listában")

#A program tároljon el egy szót egy változóban, majd írja ki egymás alá a szóban található betűket.

szo = "valami"

for betu in szo:
  print(betu)

#A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse el, hogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!

szo = "valami"
betu = input("Adj meg egy betűt: ")

if betu in szo:
  print("Ez a betű megtalálható a szóban ")
else:
  print("Ez a betű nem található meg a szóban")

#Fejlesszük tovább a 2.2 programot úgy, hogy a felhasználónak többször is legyen lehetősége újabb tippet megadnia. A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt! Igyekezz minél felhasználóbarátabbá tenni a programot! A programnak lehetnek egyéb hasznos funkciói, például gyűjtheti és kiírhatja a jó és a rossz tippeket (betűket).

szo = "valami"
jo_betuk = []
rossz_betuk = []


while True:
  betu = input("Adj meg egy betűt: ")
  if betu == "":
    break
  if betu in szo:
    jo_betuk.append(betu)
    print(f"Jó betűk: {jo_betuk}")
    print("Ez a betű megtalálható a szóban ")
    szo.replace(betu, "")
  else:
    rossz_betuk.append(betu)
    print(f"Rossz betűk: {rossz_betuk}")
    print("Ez a betű nem található meg a szóban")

#Fejlesszük tovább a 2.3 programot úgy, hogy a program egy listában tároljon öt darab szót, és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.

from random import choice
szo = 'mindenható'
lista = [szo, 'alma', 'kutya', 'béka', 'tanulás']
kivalaszt = choice(lista)
eltalalta = []
nemtalaltael = []


while True:
    felhasznalo = input('Adj meg egy betűt: ')
    if felhasznalo in kivalaszt:
        print('Eltaláltad!')
        eltalalta.append(felhasznalo)
        print(eltalalta)
    else:
        print('Nem találtad el!')
        nemtalaltael.append(felhasznalo)
        print(nemtalaltael)
    if felhasznalo == '':
        break
    
    
print('A szó:', kivalaszt)