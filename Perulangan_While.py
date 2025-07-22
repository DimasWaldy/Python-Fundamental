# Program Perulangan dengan While

jumlah_buku = 10
print('Ibu berkata, "Baca semua buku mu"')

jumlah_yang_sudah_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_yang_sudah_dibaca} sudah dibaca")

while jumlah_yang_sudah_dibaca < jumlah_buku:
    jumlah_yang_sudah_dibaca = jumlah_yang_sudah_dibaca + 1
    print(f"Buku ke {jumlah_yang_sudah_dibaca} sudah dibaca")

print("       ")
print(f"Jumlah buku yang sudah dibaca {jumlah_yang_sudah_dibaca}")