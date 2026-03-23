aparelho = input("\nDigite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * 0.75  # valor fixo: R$ 0,75 por kWh

print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")