#No. 1
def lulus_saja(hasil_akhir):
    lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]
    return lulus

hasil_akhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]

hasil = lulus_saja(hasil_akhir)
print("Hasilnya:", hasil)
