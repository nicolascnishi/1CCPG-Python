temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

limiteCritico = 33

maiorQuantidade = -1
salaMaiorRisco = 0

for indice, temperaturasSala in enumerate(temperaturas):

    numeroSala = indice + 1

    media = sum(temperaturasSala) / len(temperaturasSala)

    registrosCriticos = 0
    for temp in temperaturasSala:
        if temp >= limiteCritico:
            registrosCriticos = registrosCriticos + 1

    print(f"Sala {numeroSala}")
    print(f"Média: {media}")
    print(f"Registros críticos: {registrosCriticos}")
    print()

    if registrosCriticos > maiorQuantidade:
        maiorQuantidade = registrosCriticos
        salaMaiorRisco = numeroSala

    # Mostra a sala com maior risco
    print(f"Sala com maior risco: Sala {salaMaiorRisco}")
