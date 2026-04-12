print("-"*33)
print(" Pesquisa de Opinião por TudoWeb")
print("-"*33)

excelente = 0
ruim = 0

for i in range(50):
    print(f"Entrevistado nº{i+1}")
    print("-"*18)
    nome = input("Digite seu nome.\nR: ")
    idade = int(input("\nDigite sua idade.\nR: "))
    opiniao = int(input("\nQual o seu grau de satisfação com o nosso atendimento? \n(1)EXCELENTE   (2)BOM   (3)RUIM \nR: "))
    print("\n"+"-"*18)

    if opiniao == 1:
        excelente +=1
    elif opiniao == 3:
        ruim +=1

print("    RESULTADOS    ")
print("-"*18)
print("Quantidade de respostas 'EXCELENTE':", excelente)
print("\nQuantidade de respostas 'RUIM':", ruim)