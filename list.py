daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking']
print('Tampilka variable daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada index tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilam dengan for i in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# variable pada python bisa berisi tipe data acak seperti angka, koma, huruf
daftar_buku = [1, 'Anjay', -10, 3.14]
print('\nTampilkan dengan for in range, di mana tipe data tiap element berbeda-beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking']
print('\nTambahkan 1 buku baru')
daftar_buku.append('buku sekolah')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nClear List")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print("\nGanti elemen Pertama")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking']
daftar_buku[0]  = 'Matematika'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nAmbil elemen ke-2")
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMencetak buku yang tadi diambil")
print(buku)

print("\nPop")
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPop -1")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking']
daftar_buku.pop(-3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension start")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking']
del daftar_buku[0:2]
# 0 (digunakan untuk memulai menghapusnya mulai dari mana) : 2 buku yang dihapus dari urutan 0 ada 2
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension start")
daftar_buku = ['Harry potter', 'Game of Thrones', 'Cooking', 'Matematika']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])