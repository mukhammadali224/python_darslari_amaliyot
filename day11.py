#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 09:25:28 2026

@author: admin
"""

car_0 = {'model' : 'Ferari', 'rang' : 'qizil'}
print(car_0['model'])
en_uz = {'apple' : 'olma', 'apricot' : 'shaftoli', 'power' : 'kuch' }
print(en_uz['apple'])
mevalar = {'olma' :10000, 'nok' :8000, 'tarvuz' :20000  }
print(f" Olma narhi {mevalar['olma'] } som")
talaba = {'ism' : 'sardor', 'yosh' : '21', 't_yil' : '2004' }
print(f"Tlabani ismi {talaba['ism'].title()} \
      yoshi {talaba['yosh']} da  \
     {talaba['t_yil']} chi yili tugilgan")
talaba['kurs'] = 3
talaba['fakultet'] = 'informatika'
talaba['ism'] = 'Abdulloh'

otam = {'ism' : 'Adahamjon', 't_yil' : '1980', 't_shahar' : 'Osh'}
print(f"Otamni ismi {otam['ism']}, {otam['t_yil']} chi yili {otam['t_shahar']} shahrida tugulgan")
s_taomlar = {'ahror'   : 'osh',
             'akmal'   : 'dimlama',
             'shavkat' : 'shorva',
             'gani'    : 'mastava',
             'bobur'   : 'somsa' }
for odam, taom in s_taomlar.items():
    print(f"{odam.title()}ni sevimli taomi {taom}")
print(f"Ahrorni sevimli taomi {s_taomlar['ahror']}")
print(f"Ganini sevomli taomi {s_taomlar['gani']}")
print(f"Boburni sevimli taomi {s_taomlar['bobur']}")
print(f"Shavkatni sevimli taomi {s_taomlar['shavkat']}")
python_lugat = {'integer' : 'butun son',
                'float'   : 'kasrli son',
                'del'     : 'ochirib tashlash',
                'for in'  : 'takrorlash',
                'if else' : 'agar aks holda',
                'remove'  : 'ochirib tashllash',
                'append'  : 'yuklash',
                'insert'  : 'yuklash nomer bilan',
                'len'     : 'sanash',
                'range'   : 'sanash'}


kalit_soz = input("Kalit soz kiriting\n>>>").lower()
kalit = python_lugat.get(kalit_soz )
if kalit == None:
    print(f" {kalit_soz} degan kalit soz mavjud emas")
else:
    print(f"{kalit_soz}ni manosi {kalit}" )


        Qoshimcga mashgulot

#1. Телефонная книга

telefon_nomerlar = {'ali'   : '0556843922',
                    'akmal' : '0777879222',
                    'aziz'  : '0545839923',
                    'obid'  : '0444727383',
                    'zuhro' : '0999423424'
                    }
ism = input("ismni kiriting\n>>>").lower()
user = telefon_nomerlar.get(ism)
if user==None:
    print("Odam topilgani yoq")
else:
    print(f"Foydalanuvchini nomeri : {user}")

#2. Цены на продукты

mevalar = {'olma' : 50, 'banan' : 35, 'behi' : 100,
           'shaftoli' : 20, 'uzum' : 200}
savat = input('tanlang\n>>>').lower()
meva = mevalar.get(savat)
if meva==None:
    print('Bunday meva yoq')
else:
    print(f"{meva}")

#3. Счётчик букв

wotermelon = {'w':1, 'o':2, 't':'1', 'e':'2', 'r':'1', 'm':'1','l':'1', 'n':'1'}
for soz,son in wotermelon.items():
    print(f"wotermelon sozida {soz} harifi {son} marta keladi")

#5. Переводчик

en_uz = {'apple':'olma', 'phone':'telefon', 'green':'yashil', 'boy':'bola',
         'girl':'qiz', 'child':'godak', 'home':'uy', 'car':'moshina'}
wordd = input("Soz kiritish\n>>>").lower()
word = en_uz.get(wordd)
if word is None:
    print('Bu soz topilmadi')
else:
    print(f"Tarjimasi {word}")
    
    
soz = "watermelon"
hisob = {}
for harf in soz:
    if harf in hisob:
        hisob[harf] += 1
    else:
        hisob[harf] = 1

for harf, son in hisob.items():
    print(f"{soz} so'zida {harf} harfi {son} marta keladi")
    


meals = {'osh':150, 'kabob':120, 'somsa':100, 'mastava':70, 'shorva':130}
jami_summa = 0
for i in range (1,4):
    meal=input(f"{i} birinchi taomni kiriting")
    narh = meals.get(meal)

    if narh is None:
             print('Bunday taom yoq')
    else:
             jami_summa+=narh
             print(f"{meal.title()} narhi {narh}")
print(jami_summa)
🔟 Мини-экзамен

Создай словарь Python-терминов (int, float, for, if).
Пользователь вводит термин → выведи объяснение.

python_sozlar = {'integer' : 'butun son',
                'float'   : 'kasrli son',
                'del'     : 'ochirib tashlash',
                'for in'  : 'takrorlash',
                'if else' : 'agar aks holda',
                'remove'  : 'ochirib tashllash',
                'append'  : 'yuklash',
                'insert'  : 'yuklash nomer bilan',
                'len'     : 'sanash',
                'range'   : 'sanash'}
tarjima = input("Sozni kiriting\n>>>")
soz = python_sozlar.get(tarjima)
if soz is None:
    print("Bunday soz yoq ")
else:
    print(f"{tarjima} sozini tarjimasi {soz} ")

market = {'osh':150, 'kabob':120, 'somsa':100, 'mastava':70, 'shorva':130}
jami_summa = 0
for i in range(1,4):
    mahsulotlar = input(f"{i} chi mahsulotni kiriting\n>>>").lower()
    
    mahsulot = market.get(mahsulotlar)
    if mahsulot is None:
        print("Bunday mahsulot yoq")
    else:
        jami_summa+=mahsulot

print(jami_summa,'jami summa')
















































