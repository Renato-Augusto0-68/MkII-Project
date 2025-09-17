import numpy as np; import sympy as sp
from modules import operation, bincon, recon,limit,factor
print("Mark II, versão 1.52.00")
print("Criado por Rutheford")
print ("o que você gostaria de fazer?")

A=float(input("Number: "))
operation(A)

print("MKII fatorial calculator")
numero=int(input("Digite o número para realizar o fatorial: "))
print(f"O fatorial do número {numero}, é {factor(numero)}")

print ("Preparando modo binário/Octal/hexadecimal:")
print ("Modo binário/octal/hexadecimal. Version 1.0")
b=int(input("Escolha a base numérica (2,8,16): "))
bincon(b)

print ("Retro-Modo binário/octal/hexadecimal. Version 1.0")
b_2=int(input("Digite a base numérica [2,8,16]: "))
recon(b_2)

print("MkII limit calculator")
print("version 1.0")
kl=sp.Symbol('x')
limit(kl)