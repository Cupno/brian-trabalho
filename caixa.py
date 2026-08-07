quantidade = int(input("Quantidade de itens: "))

if quantidade <= 0:
    print("A quantidade deve ser maior que zero.")
else:
    total = 0

    for i in range(1, quantidade + 1):
        preco = float(input(f"Preço do item {i}: R$ "))

        if preco < 0:
            print("Preço inválido.")
            break

        total += preco
    else:
        media = total / quantidade

        print("\n===== RESULTADO =====")
        print(f"Total da compra: R$ {total:.2f}")
        print(f"Média por item: R$ {media:.2f}")
