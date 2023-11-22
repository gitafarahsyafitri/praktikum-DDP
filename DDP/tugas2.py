def kelulusan(nilai):
    if nilai <=60:
        return "gagal"
    elif nilai >= 61 and nilai <=70:
        return "baik"
        
    elif nilai >=71 and nilai <=80:
        return 'sangat baik'
    elif nilai >=81 and nilai <=100:
        return "istimewa"
    
print(kelulusan(60))