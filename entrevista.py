TOTAL_ENTREVISTADOS = 50

excelente = 0
ruim = 0

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    print("Como você avalia o atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Opinião (1, 2 ou 3): "))

    while opiniao not in (1, 2, 3):
        print("Opção inválida! Digite 1, 2 ou 3.")
        opiniao = int(input("Opinião (1, 2 ou 3): "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\n===== RESULTADO DA PESQUISA =====")
print(f"Respostas EXCELENTE: {excelente}")
print(f"Respostas RUIM: {ruim}")
