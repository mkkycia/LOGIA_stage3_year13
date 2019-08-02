def ileod(liczba):
    a = ''
    suma = 0
    b = 0
    c = ''
    for i in range(len(liczba)):
        if i % 2 == 0:
            a += '1'
        else:
            a += '0'
    if int(a) > int(liczba):
        a = a[:-1]
    for i in range(len(a)):
        suma = 2 * suma + int(a[i])
    for i in range(len(liczba)):
        b = 2 * b + int(liczba[i])
    return bin(abs(suma - b))[2:]

    

print(ileod("101"))
print('expected 0')
print('===========================')
print(ileod("111"))
print('expected 10')
print('===========================')
print(ileod("1101"))
print('expected 11')
print('===========================')
print(ileod("1"))
print('expected 0')
print('===========================')
print(ileod("1001111"))
print('expected 100101')
print('===========================')
print(ileod("110000"))
print('expected 110')
print('===========================')
print(ileod("111111111111011"))
print('expected 10101010100110')
print('===========================')
print(ileod("10101010101101010"))
print('expected 10101')
print('===========================')
print(ileod("100000000000000000000000000000"))
print('expected 1010101010101010101010101011')


