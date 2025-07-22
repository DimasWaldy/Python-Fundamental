# Sequential
print('Ibu menyuruh Budi ke toko untuk membeli susu')
print('Ibu berkata "Jika ada telur beli 6"')
print('Budi mengiyakan dan pergi ke toko')
print('Budi melihat stok susu dan harga susu')

# Percabangan
jumlah_stok_susu = 100
harga_susu = 1500
jumlah_telur = 1535
print(f"Jumlah botol susu {jumlah_stok_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_stok_susu > 0:
    print("Budi melihat stok susu dan harganya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Memberi hasil belanjaan ke Ibu")