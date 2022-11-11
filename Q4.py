# função para converter o número
def toStr(n, base):
    # variável que armazena os caracteres hexadecimais
    convertStr = "0123456789ABCDEF"
    if n < base:
        return convertStr[n]
    else:
        return toStr(n // base, base) + convertStr[n % base]


# conversão dos números para hexadecimal
print(toStr(2022, 16))
print(toStr(2023, 16))
