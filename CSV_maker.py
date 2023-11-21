import pandas as pd
import numpy as np
import math as mt

# TOTO: 
#   Código que pegue a versão .txt dos pdfs das matriculas e transforma em um csv, com o RA do aluno e a disciplina matriculada, de
#   preferencia determinar um codigo universal pras disciplinas, de forma que possamos identificar qual disciplina é com isso

t = open("test.csv", "w")
t.write("")
t.close()


a = open("test.txt", "r", encoding="utf-8")
b = open("test.csv", "a", encoding="utf-8")

#for i in a.read():
#    k = "a"
#    while i == "\n" and k == "a": k = input()
#    print(i, end="")

cont = 0

for i in a:

    ins = ""

    cont+= 1

    if cont <= 2: 
        # print(i)
        b.write(i)
        continue
    else:
        if not i[0].isnumeric() or i[2] == "/" or i[3] == "/" or i[4] == "/": continue
 
    l = 0

    RA = ""
    disc = ""

    while i[l] != " ": 
        RA+= i[l]
        l+=1
    l+=1

    while not i[l-1].isnumeric():
        disc+= i[l]
        l+=1
    
    while i[l] != "-": l+=1
    l+= 3
    
    for n in range(2): disc+=i[l+n]

    l+=2

    while i[l+2] != '-':
        if i[l-1] == " " and i[l].isupper(): disc+= i[l]
        l+=1

        if l > len(i) - 4: break

    # print(RA)
    # print(disc)

    ins+= RA
    ins+= ", "
    ins+= disc
    ins+= "\n"

    b.write(ins)

    
a.close()
b.close()