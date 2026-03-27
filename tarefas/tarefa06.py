ad = []
while True:
    num = input("digite um numero :")
    if num.lower() == 'para':
        break
    else:
        ad.append(int(num))
        print(f"numeros adcionados; {ad}")
        