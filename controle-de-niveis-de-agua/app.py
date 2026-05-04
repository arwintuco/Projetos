from colorama import Fore, Style

print("="*28)
print(" Controle de Níveis de", Fore.CYAN + "Água")
print(Style.RESET_ALL + "="*28)

mensagens = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

def cor_nivel(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Style.RESET_ALL

print("\nNíveis do Reservatório")
for i, msg in enumerate(mensagens, start=1):
    print(f"Nível {i}: {cor_nivel(i)}{msg}{Style.RESET_ALL}")

print("\n" + "="*50)
nivel_atual = 0
while nivel_atual < 1 or nivel_atual > 5:
    nivel_atual = int(input("Digite o nível atual do reservatório (1 a 5): "))
    if nivel_atual < 1 or nivel_atual > 5:
        print("Valor inválido! Digite um número entre 1 e 5\n")

print("Situação atual do reservatório:")
print(f"Nível {nivel_atual}: {cor_nivel(nivel_atual)}{mensagens[nivel_atual-1]}{Style.RESET_ALL}")
print("="*50)