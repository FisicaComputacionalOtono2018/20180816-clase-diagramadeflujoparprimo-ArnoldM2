#Alumno: Arnold Morales Morales
#Fecha: 16 de Agosto de 2018
#

def primo(num):
    flag = True	
    if num<2:
       flag=False
    elif p==2:
       flag=True
    else:	
     for i in range (2,num-1/2):         
	if num%i==0:
            flag=False
            break
    return flag

p=input ("Dame un numero: ")

if primo(p):
   print ("El numero es primo")
else:
   print ("El numero no es primo")
   
 
