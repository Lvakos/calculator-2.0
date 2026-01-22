from moodul import *
while True:
    try:
        a = float(input("Kirjuta esimene arv: "))
        b = float(input("Kirjuta teine arv: "))
        if a < 0 or b < 0:
            print("Kirjuta ainult taisarv!")
            continue
        else:
            break
    except ValueError:
        print("Kirjuta ainult arv")
        continue

while True:
    deystvie = input("Выбери действие (*, /, +, -, квадрат: ")
    if deystvie == "*":
        print(umnozit(a, b))
        break
    elif deystvie == "/":
        print(podelit(a, b))
        break
    elif deystvie == "+":
        print(slozit(a, b))
        break
    elif deystvie == "-":
        print(minus(a, b))
        break
    elif deystvie.lower() == "квадрат":
        break
    else:
        continue
    
if deystvie == "квадрат":
    while True:
        choose = input("Какое число ты хочешь возвести в квадрат(1 или 2): ")
        if choose == "1":
            print(kvadrat(a))
            break
        elif choose == "2":
            print(kvadrat(b))
            break
        else:
            continue