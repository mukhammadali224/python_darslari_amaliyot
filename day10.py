#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 14:28:45 2026

@author: admin
"""
#xatolar ustida ishlash
son = int(input("Juft son kiriting: "))
if son%2==0:
    print("Rahmat") 
else:
    print(f"Bu {son} juft emas.")


yosh = (int(input("Yoshingiz nechida?")))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
    
print(f"Chipta {narh} so'm")
   
x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}") 
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower())

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot.title()} bor")
        else:
            print(f"Do'konimizda {mahsulot.title()} yo'q")
else: 
    print("Savatingiz bo'sh")   
mahsulotlar_set = {'un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun'}


savat = []
for n in range(5):
   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower())

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar_set:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)

else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


users = ['alisher1983','aziza','yasina', 'umar']

login = input("Yangi login tanlang:")

if login.lower() in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")
        









































