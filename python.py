# Задание №1       #Вариант 9 на всех заданияx.
from math import *
x= float(input("Введите число x:"))
y= float(input("Введите число y:"))
z= float(input("Введите число z:"))

otvet = abs(x**(y/x)-((y/x)**(1./3.)))+ (y-x)*(cos (y - z)/(y-x))/(1 +pow(y-x,2))
print (otvet)

#Задание №2
mecyac= int(input(" Введите число "))
print(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
       'December'][int(input()) - 1])
#Задание №3
n = 100
for i in range(1, 150):
 if i*i > n:
  print(i*i)
  break
        
n = 100
num = 1
while num < n:
    for i in range(4,16):
        num += i
    
print(num)
