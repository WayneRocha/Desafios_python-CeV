# calcular o IMC de uma pessoa e mostrar se seu estado é... abaixo de 18,5(abaixo do peso) | 18,5 a 25(peso ideal) |
# 25 a 30(sobrepeso) | 30 a 40(obesidade) | acima de 40(obesidade mórbida)

print('=========MINISTERIO DA SAÚDE===========')
peso = float(input('Quanto você pesa? '))
altura = float(input('Qual a sua altura(Ex1.50)? '))
imc = peso / altura ** 2
print('-' * 40)
if imc < 18.5:
    print('Você está abaixo do peso')
    print('Procure um nutricionista')
elif 18.5 < imc <= 25:
    print('Você está com peso ideal!')
    print('Continue com uma vida saudavel')
elif 25 < imc <= 30:
    print('Você está com sobrepeso')
    print('Procure um nutricionista')
elif 30 < imc <= 40:
    print('Você está em obesidade')
    print('\033[1mProcure um nutricionista o mais rápido possivel!\033[m')
else:
    print('Você está em obesidade morbida!')
    print('\033[1mProcure um nutricionista \033[31mIMEDIATAMENTE!\033[m')
