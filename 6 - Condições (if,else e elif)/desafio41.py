# ler o ano de nascimento de um atleta e mostrar sua categoria, sendo...
# até 9 anos(mirin) | até 14(infantil) | até 19(junior) | até 20(senior) | acima de 21(master)

anos = int(input('Quantos anos você tem? '))
print('-' * 25)
if anos <= 9:
    print('você ficará na categoria \033[1:7:30mMirin\033[m')
elif 14 >= anos > 9:
    print('você ficará na categoria \033[1:7:30mInfantil\033[m')
elif 14 < anos <= 19:
    print('você ficará na categoria \033[1:7:30mJunior\033[m')
elif anos == 20:
    print('você ficará na categoria \033[1:7:30mSenior\033[m')
else:
    print('você ficará na categoria \033[1:7:30mMaster\033[m')
