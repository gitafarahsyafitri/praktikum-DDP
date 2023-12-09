import math

#Tambah
def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print('penjumlahan ', bil1, "+", bil2, '=', hasil)
#kurang
def kurang(bil1, bil2):
    hasil = (bil2 - bil2 )
#pangkat, math.pow
def pangkat(bilangan1, pangkat):
    print('pangkat',bilangan1, '^', pangkat , 'adalah',math.pow(2,3))
#kali
def perkalian(bil1, bil2):
    hasil = (bil1 * bil2)
    print('perkalian', bil1, '*', bil2, '=', hasil)
#bagi
def pembagian (bil1, bil2):
    hasil =bil1 / bil2
    print('pembagian', bil1, '/', bil2, '=', hasil)
#log, math.log
def log (bil):
    print('log dari', bil, 'adalah', math.log(bil))
#akar, math.sqrt
def akar (bil):
    print('akar dari', bil, 'adalah', math.log(bil))
#sin,
def sin(bil):
    print('sin dari', bil, 'adalah', math.sin(bil))
#cos,
def cos(bil):
    print('cos dari', bil, 'adalah', math.cos(bil))
#Tan,
def tan (bil):
    print('tan dari', bil, 'adalah', math.tan(bil))