def calcular_reajuste(salario_atual):
    # Definindo os percentuais de aumento
    if salario_atual <= 280:
        percentual_aumento = 20
    elif salario_atual <= 700:
        percentual_aumento = 15
    elif salario_atual <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5

    # Calculando o valor do aumento
    valor_aumento = salario_atual * (percentual_aumento / 100)
    
    # Calculando o novo salário
    novo_salario = salario_atual + valor_aumento
    
    # Calculando o valor do aumento real, descontando a inflação
    inflacao = 3.8
    valor_aumento_real = valor_aumento - (valor_aumento * (inflacao / 100))
    
    # Exibindo os resultados
    print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"Valor do aumento: R$ {valor_aumento:.2f}")
    print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")
    print(f"Valor do aumento real, descontado a inflação: R$ {valor_aumento_real:.2f}")

# Exemplo de uso
salario_atual = float(input("Digite o salário atual do colaborador: "))
calcular_reajuste(salario_atual)