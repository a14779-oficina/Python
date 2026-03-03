# Exercício B1 - Número Positivo ou Negativo
# Criar um programa que:
# Peça um número ao utilizador
# Indique se é positivo ou negatito

numero = int(input("Digite um número: "))

if numero >= 0:
     print("Número positivo")
else:
     print("Número negativo")

# Exercício B2 - Maior de Idade
# Criar um programa que:
# Peça a idade
# Indique se é maior ou menor de idade
# Regra:
# Maior ou igual a 18 → Maior de idade

idade = int(input("Digite a sua idade: "))

if idade >= 18:
     print("Maior de idade")
else:
     print("Menor de idade")

# Exercício B3 - Número Par ou Ímpar
# Criar um programa que:
# Peça um número
# Indique se é par ou ímpar

num = int(input("Insira o número: "))

if num % 2 == 0:
     print("Número par")
else:
     print("Número ímpar")

# Exercício B4 - Comparação de Dois Números
# Criar um programa que:
# Peça dois números
# Indique qual é o maior

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

if num_1 > num_2:
     print(f"O maior número é: {num_1}")
elif num_2 > num_1:
     print(f"O maior número é: {num_2}")

# Exercício B5 - Password Simples
# Criar um programa que:
# Peça uma password
# Se for "python" → acesso permitido
# Senão → acesso negado

password = str(input("Digite a palavra-passe: "))

password_correta = "python"

if password == password_correta:
     print("Acesso autorizado!")
else:
     print("Acesso negado!")

# Exercício I1 - Classificação de Nota
# Criar um programa que:
# Peça uma nota (0 a 20)
# Mostre:
# >= 18 → Excelente
# >= 14 → Bom
# >= 10 → Suficiente
# < 10 → Reprovado

nota = int(input("Digite a nota: "))

if nota >= 18:
     print("Excelente!")
elif nota >= 14:
     print("Bom")
elif nota >= 10:
     print("Suficiente")
else: 
     print("Reprovado!")

# Exercício I2 - Classificação de Idade
# Criar programa que classifique:
# < 13 → Criança
# 13-17 → Jovem
# 18-64 → Adulto
# 65+ → Sénior

idade1 = int(input("Digite a sua idade: "))

if idade1 < 13:
     print("Criança")
elif idade1 >= 13 and idade1 <= 17:
     print("Jovem")
elif idade1 >= 18 and idade1 <= 64:
     print("Adulto")
else:
     print("Sénior")

# Exercício I3 - Múltiplo de 3 e 5
# Criar programa que:
# Peça um número
# Indique:
# Múltiplo de 3
# Múltiplo de 5
# Múltiplo de ambos
# Nenhum

nums = int(input("Digite um número: "))

if nums % 3 == 0 and nums % 5 == 0:
     print("Múltiplo de 3 e de 5")
if nums % 3 == 0:
     print("Múltiplo de 3")
elif nums % 5 == 0:
     print("Múltiplo de 5")
else:
     print("Nenhum")

# Exercício I4 - Login com Utilizador e Password
# Sistema com:
# Utilizador correto: admin
# Password correta: 1234
# Verificar ambos.

username = str(input("Digite o nome de utilizador: "))
pass_word = int(input("Digite a palavra-passe: "))

username_correto = "admin"
password_certa = 1234

print(username == username_correto and password == password_correta)

# Exercício I5 - Número dentro de intervalo
# Criar programa que:
# Peça um número
# Indique se está entre 10 e 20

num1 = int(input("Digite um número: "))

if num1 >= 10 and num1 <= 20:
     print("Está no intervalo entre 10 e 20")
else:
     print("Não está no intervalo entre 10 e 20")

# Exercício A1 - Sistema Multibanco Simples
# Criar programa que:
# Defina saldo inicial = 1000
# Peça valor a levantar
# Se saldo suficiente → autorizado
# Senão → saldo insuficiente

saldo = 1000
valor_levantar = int(input("Digite a quantia que deseja levantar: "))
saldo_restante = saldo - valor_levantar

if valor_levantar <= saldo:
     print("Autorizado!")
else:
     print("Saldo insuficiente!")

# Exercício A2 - Maior de Quatro Números
# Criar programa que:
# Peça 4 números
# Mostre o maior

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))
num_4 = int(input("Digite o quarto número: "))

if num_1 >= num_2 and num_1 >= num_3 and num_1 >= num_4:
     print(f"O maior número é: {num_1}")
elif num_2 >= num_1 and num_2 >= num_3 and num_2 >= num_4:
     print(f"O maior número é: {num_2}")
elif num_3 >= num_1 and num_3 >= num_2 and num_3 >= num_4:
     print(f"O maior número é: {num_3}")
else: 
     print(f"O maior número é: {num_4}")

# Exercício A3 - Classificação de IMC (Simplificado)
# Fórmula:
# IMC = peso / (altura × altura)
# Classificação:
# < 18.5 → Baixo peso
# 18.5–24.9 → Normal
# 25–29.9 → Excesso de peso
# >= 30 → Obesidade

peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Baixo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("Excesso de peso")
else:
    print("Obesidade")

# Exercício A4 - Sistema de Desconto
# Criar programa que:
# Peça valor da compra
# Aplicar desconto:
# >= 100 → 10%
# >= 50 → 5%
# < 50 → sem desconto
# Mostrar valor final.

valor_compra = int(input("Digite o valor da compra: "))
desconto = 0

if valor_compra >= 100:
    desconto = valor_compra * 0.1
    valor_final = valor_compra - desconto
    print(f"O valor da compra é {valor_final} porque foi aplicado um desconto de 10%")
elif valor_compra <= 50:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f"O valor da compra é {valor_final} porque foi aplicado um desconto de 5%")
else:
    print("Não teve direito a desconto.")

# Exercício A5 - Verificação de Ano Bissexto (Simplificado)
# Criar programa que:
# Peça um ano
# Verifique se é divisível por 4

# Se for → Ano bissexto
# Senão → Ano normal

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("Ano bissexto")
else:
    print("Ano normal")