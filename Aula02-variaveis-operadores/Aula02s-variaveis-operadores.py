print("Hello World")

print(7 +4)

print("7" + "4") #CONCATENANDO STRINGS

#COMENTARIO DE 1 LINHA
'''
    Comentário de multiplas linhas
'''
#VARIÁVEIS
nome = "Nicolas" # str = texto
idade = 18 #int = numeros inteiros
peso = 64.4 #float = numeros quebrados

print(nome, idade, peso)

print(f"Olá, {nome}!!!") #f = formatar

#input = simulação de um forms no cmd
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento= 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Sua idade é {idade}")