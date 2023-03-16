Coin = int(input('Введите число монеток:'))
gerb = reshka = 0
for i in range(Coin):
    x = int(input('герб(1) или решка(0)? '))
    if x == 1:
        gerb += 1
    else:
        reshka += 1
if gerb < reshka:
    print(f'Переверните {gerb} монетку с герба на решку, их меньше всего')
elif gerb == reshka:
    print(f'Количество гербов и решек одинаково, по {gerb} штук')
else:
    print((f'Переверните {reshka} монетку с решки на герб, их меньше всего'))