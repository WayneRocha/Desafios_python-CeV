def leiaInt(msg='Digite um valor inteiro: '):
    while True:
        try:
            val = int(input(msg))
        except KeyboardInterrupt:
            val = 0
            break
        except ValueError:
            print('\033[31mDigite um valor inteiro!\033[m')
            continue
        else:
            return val


def leiaFloat(msg='Digite um valor real: '):
    while True:
        try:
            val = str(input(msg)).replace(',', '.')
            val = float(val)
        except KeyboardInterrupt:
            val = 0.0
            return val
        except ValueError:
            print('\033[31mDigite um valor real!\033[m')
            continue
        except:
            print('\033[31mOcorreu um erro! tente novamente!\033[m')
            continue
        else:
            return val


inteiro = leiaInt()
real = leiaFloat()
print(f'Você digitou o valor inteiro {inteiro}')
print(f'Você digitou o valor real {real}')
