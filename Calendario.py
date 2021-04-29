dia = int(input("Insira um dia: "))
print("----------------------------")
mes = int(input("Insira um mês: "))
print("----------------------------")
ano = int(input("Insira um ano: "))

bissexto = False

if ano%4 == 0:
    bissexto = True

if bissexto == True and mes == 2 and dia > 29:
        print("----------------------------")
        print("A data inserida é INVÁLIDA!")
elif bissexto == False and mes == 2 and dia > 28:
        print("----------------------------")
        print("A data inserida é INVÁLIDA!")
elif dia <= 0 or dia > 31:
    print("----------------------------")
    print("A data inserida é INVÁLIDA!")
elif mes == 4 and dia > 30 or mes == 6 and dia > 30 or mes == 9 and dia > 30 or mes == 11 and dia > 30:
    print("----------------------------")
    print("A data inserida é INVÁLIDA!")
elif mes <= 0 or mes > 12:
    print("----------------------------")
    print("A data inserida é INVÁLIDA!")
elif ano <=0 or ano > 9999:
    print("----------------------------")
    print("A data inserida é INVÁLIDA!")
else:
    print("----------------------------")
    print("A data inserida é: ", dia, "/", mes, "/", ano, "e ela é VÁLIDA!")
