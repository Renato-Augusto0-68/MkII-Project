def operation(A): #the choose of what to do with the two numbers
 while True:
    B=float(input("Number two: "))
    decis=str(input("Digite a operação que você gostaria de fazer: ")).lower()
    if decis=='+':
        Soma=lambda A,B: A+B
        col=Soma(A,B)
        print (f"resultado A + B= {Soma(A,B)}")
 
    elif decis=='-':
        Subtração = lambda A,B: A-B
        col=Subtração(A,B)
        print(f"Novo resultado= {(Subtração(A,B))}")
 
    elif decis=='*':
        Mult=lambda A,B: A*B
        col=Mult(A,B)
        print (f"Resultado da Multiplicação= {Mult(A,B)}")
 
    elif decis=='/':
        div=lambda A,B: A/B
        col=div(A,B)
        print (f"Resultado da divisão= {div(A,B)}") 
  
    elif decis=='exponencial':
        Exponencial = lambda A,B: A**B
        col=Exponencial(A,B)
        print (f"Resultado da potenciação={Exponencial(A,B)}")
 
    elif decis=='modulo':
        Módulo = lambda A,B: A%B
        col=Módulo(A,B)
        print (f"Resultado do módulo= {Módulo(A,B)}")
    A=col
    control=bool(input("Continue? (True/False): "))
    if control==False: break

def factor(numero):
 if numero==0 ^ numero==1:
    return 1
 elif numero<0:
    print("Resultado inválido")
 else:
   return numero*factor(numero-1)

def bincon(b):
 import math as mth
 numbr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 for n in range(1,14):
     numbr[n]=int(input(f"digito boh {n}: ")) 
     if (numbr[n]>(b-1)): exit()
 Total = (mth.pow(b,15-1)*numbr[0]) +(mth.pow(b,15-2) *numbr[1])+(mth.pow(b,15-3) *numbr[2])+(mth.pow(b,15-4) *numbr[3])+ (mth.pow(b,15-5) *numbr[4])+(mth.pow(b,15-6) *numbr[5])+(mth.pow(b,15-7) *numbr[6])+(mth.pow(b,15-8) *numbr[7])+(mth.pow(b,15-9) *numbr[8])+(mth.pow(b,15-10) *numbr[9])+(mth.pow(b,15-11) *numbr[10])+(mth.pow(b,15-12) *numbr[11])+(mth.pow(b,15-13) *numbr[12])+ (mth.pow(b,15-14)*numbr[13]) +(mth.pow(b,15-15)*numbr[14])
 print(f"Aqui está seu número:{Total}, em base 10. Originalmente estava na base {b}, como {numbr}")

def recon(b_2):
 convers=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 convers[0]=int(input("Digite o número para converter: "))
 for n in range(1,14):
   convers[n]=convers[n-1]//b_2
 Total2=((convers[13]%b_2), (convers[12]% b_2), (convers[11]%b_2), (convers[10]%b_2), (convers[9]%b_2), (convers[8]%b_2), (convers[7]%b_2), (convers[6]%b_2), (convers[5]%b_2), (convers[4]%b_2), (convers[3]%b_2), (convers[2]%b_2), (convers[1]%b_2), (convers[0]%b_2))
 print (f"Aqui está seu número:{Total2}, em base {b_2}. Originalmente estava na base 10, como {convers[0]}")

def limit(kl):
   import sympy as sp
   valores_lim=[0,0,0,0,0,0]
   for n in range(5):
      print(f"equação: ((({kl}**{valores_lim[0]})+{kl}*{valores_lim[1]}+{valores_lim[2]})/(({kl}**{valores_lim[3]})+{valores_lim[4]}*{kl}+{valores_lim[1]}))")
      ll=float(input("Valor para usar em variadas circunstâncias: "))
      valores_lim[n]=ll
   r=int(input(f"Digite o valor que {kl} se aproxima de: "))
   yl=(((kl**valores_lim[0])+kl*valores_lim[1]+valores_lim[2])/((kl**valores_lim[3])+valores_lim[4]*kl+valores_lim[1]))
   print(f"O valor do limite de {yl}, com x tendendo a {r}, é {sp.limit(yl,kl,r)}")