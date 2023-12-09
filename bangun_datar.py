def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("luas persegi:", luas)
    print("keliling persegi:", keliling)


def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("luas persegi panjang:", luas)
    print("keliling persegi panjang:", keliling)


def segitiga_sama_sisi(alas, tinggi):
    luas = 0.5 * alas * tinggi
    keliling = 3 * alas 
    print("luas segitiga sama sisi:", luas)
    print("keliling segitiga sama sisi:", keliling)


def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling =( 2 * alas) + (2 * sisi_miring)
    print("luas jajar genjang:", luas)
    print("keliling jajar genjang:", keliling)


def lingkaran (jari2):
    phi = 3.14
    luas = phi * jari2 ** 2 
    keliling = 2 * jari2 * phi 
    print("luas lingkaran:", luas)
    print("keliling lingkaran:", keliling)

def belah_ketupat(diagonal1,  diagonal2, sisi):
    luas = 0,5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("luas belah ketupat:", luas)
    print("keliling belah ketupat:", keliling)


def layang_layang(diagonal1, diagonal2, sisi_atas, sisi_bawah):
    luas = 0,5 * diagonal1 * diagonal2
    keliling = (2 * sisi_atas) + (2 * sisi_bawah)
    print("luas layang-layang:", luas)
    print("keliling layang-layang:", keliling)