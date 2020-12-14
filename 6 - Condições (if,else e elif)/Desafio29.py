# ver a velocidade de um carro e, se estiver a mais de 80Km/h, leva multa
# e a multa vai ser de 7R$ a cada km ultrapassado

print("Radar de velocidade")
print("=" * 30)
speed = float(input('Velocidade do carro (Km/h): '))
print('=' * 20)
if speed > 80:
    multa = (speed - 80) * 7
    print('\033[1:31mAcima do limite de velocidade!')
    print(f'Multa de {multa:.2f}R$\033[m')
else:
    print('\033[32mContinue assim!\nTenha uma ótima viagem!\033[m')
