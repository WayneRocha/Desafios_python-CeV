# ler a temperatura em graus Celsius e mostralo em fahrenheint

c = float(input('Temperatura em ºC'))
f = (c * 9/5) + 32
print('{}ºC são \033[4m{}ºFahrenheint'.format(c, f))
