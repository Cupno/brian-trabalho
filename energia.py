consumo_total = 0
dias_acima = 0

for dia in range(1, 8):
    while True:
        try:
            consumo = float(input(f"Consumo do dia {dia} (kWh): "))

            if consumo < 0:
                print("O consumo não pode ser negativo.")
                continue

            break

        except ValueError:
            print("Digite um número válido.")

    consumo_total += consumo

    if consumo > 20:
        dias_acima += 1

print("\n===== RELATÓRIO SEMANAL =====")
print(f"Consumo total: {consumo_total:.2f} kWh")
print(f"Dias com consumo acima de 20 kWh: {dias_acima}")
