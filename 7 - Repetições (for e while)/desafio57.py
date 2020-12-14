# Ler o sexo de uma pessoa e caso a digitação esteja errada pedir para digitar novamente

sexo = str(input('Digite seu sexo[F/M]: ')).upper().strip()[0]
while sexo != 'F' and sexo != 'M':
    print('\033[31mSexo invalido! ❌\033[m')
    sexo = str(input('Digite seu sexo[F/M]: ')).upper().strip()[0]
print('\033[32mSexo valido! ✔\033[m')
